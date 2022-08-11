import time
from ccxt import binance


class BinanceFut(binance):
    def __init__(binance, apiKey='', secret=''):
        super(BinanceFut, binance).__init__()
        binance.apiKey = apiKey
        binance.secret = secret

    # 获取K线
    def get_futures_klines(binance, symbol, interval, limit=500):
        '''
        :param symbol:
        :param interval: ENUM 1m，3m，5m，15m，30m，1h，2h，4h，6h，8h，12h，1d，3d，1w，1M
        :param limit: 默认500 最大1500
        :return:
        '''
        symbol = symbol.replace('/', '').upper()
        params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }
        return binance.fapiPublicGetKlines(params) if 'USDT' in symbol else binance.dapiPublicGetKlines(params)

    # 获取订单薄深度
    def get_futures_depth(binance, symbol, limit=500):
        '''
        :param symbol: BTCUSDT, BTCUSD_PERP, BTCUSD_210625
        :param limit: 默认500 最大1500
        :return:
        '''
        symbol = symbol.replace('/', '').upper()
        params = {
            'symbol': symbol,
            'limit': limit
        }
        return binance.fapiPublicGetDepth(params) if 'USDT' in symbol else binance.dapiPublicGetDepth(params)

    # 获取币对的市场最新成交信息
    def get_futures_trades(binance, symbol, limit=500):
        '''
        :param symbol: BTCUSDT, BTCUSD_PERP, BTCUSD_210625
        :param limit: 默认500 最大1500
        :return:
        '''
        symbol = symbol.replace('/', '').upper()
        params = {
            'symbol': symbol,
            'limit': limit
        }
        return binance.fapiPublicGetTrades(params) if 'USDT' in symbol else binance.dapiPublicGetTrades(params)

    # 合约--现货 保证金划转
    def transfer(binance, asset, amount, type):
        '''
        :param asset:  ENUM: BTC USDT BNB
        :param amount:  float or int
        :param type: 	1: 现货账户向USDT合约账户划转
        2: USDT合约账户向现货账户划转
        3: 现货账户向币本位合约账户划转
        4: 币本位合约账户向现货账户划转
        :return: {"tranId": 100000001}    // 划转 ID
        '''
        params = {
            'asset': asset,
            'amount': amount,
            'type': type,
            'timestamp': int(time.time() * 1000)
        }
        return binance.sapiPostFuturesTransfer(params)

    # 下单接口
    def create_futures_order(binance, symbol, side, price, amount, type='LIMIT'):
        '''
        :param symbol:  自动区分币本位和U本位：BTCUSDT（U本位永续）、BTCUSDT_210625、BTCUSD_PERP(币本位永续格式）、
        :param type:  ’LIMIT', "MARKET'
        :param side:
        :param amount:
        :param price:
        :param params:
        :return:
        '''
        symbol = symbol.replace('/', '').upper()
        params = {'symbol': symbol,
                  'side': side.upper(),
                  'type': type,
                  'price': price,
                  'quantity': amount,
                  'timeInForce': 'GTC',
                  'newClientOrderId': 'x-waACsaTa' + str(time.time()),  # 如有brokerId,可于此处替换
                  'timestamp': int(time.time() * 1000)
                  }
        return binance.fapiPrivatePostOrder(params) if 'USDT' in symbol else binance.dapiPrivatePostOrder(params)

    # 撤销指定订单
    def cancel_futures_order(binance, symbol, orderid):
        '''
        :param symbol:
        :param orderid:  系统分配的订单id号
        :return:
        '''
        symbol = symbol.replace('/', '').upper()
        params = {
            'symbol': symbol,
            'origClientOrderId': orderid,
            'timestamp': int(time.time() * 1000)
        }
        return binance.fapiPrivateDeleteOrder(params) if 'USDT' in symbol else binance.dapiPrivateDeleteOrder(params)

    # 撤销所有订单
    def cancel_all_futures_order(binance, symbol):
        symbol = symbol.replace('/', '').upper()
        params = {'symbol': symbol,
                  'timestamp': int(time.time() * 1000)
                  }
        return binance.fapiPrivateDeleteAllOpenOrders(params) if 'USDT' in symbol else binance.dapiPrivateDeleteAllOpenOrders(params)


    # 获取仓位信息
    def get_futures_positions(binance, base_type='all'):
        '''
        :param future_type:  all/usdt/coin
        :return:
        '''
        params = {
            'timestamp': int(time.time() * 1000)
        }
        position0 = binance.fapiPrivateGetAccount
        position1 = binance.dapiPrivateGetAccount
        return {
            'usdt_base_balance': position0(params)['positions'],
            'coin_base_balance': position1(params)['positions']
        } if base_type == 'all' else {
            'usdt_base_balance': position0(params)['positions']
        } if base_type == 'usdt' else {
            'coin_base_balance': position1(params)['positions']
        } if base_type == 'coin' else {}

    # 获取账户余额
    def get_futures_balances(binance, base_type='all'):
        '''
        :param future_type:  all/usdt/coin
        :return:
        '''
        params = {
            'timestamp': int(time.time() * 1000)
        }
        balance0 = binance.fapiPrivateGetBalance
        balance1 = binance.dapiPrivateGetBalance
        return {
            'usdt_base_balance': balance0(params),
            'coin_base_balance': balance1(params)
        } if base_type == 'all' else {
            'usdt_base_balance': balance0(params)
        } if base_type == 'usdt' else {
            'coin_base_balance': balance1(params)
        } if base_type == 'coin' else {}

