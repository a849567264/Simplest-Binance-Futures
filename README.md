# Simplest-Binance-Futures
Simplest Binance-Futures SDK mixing USDT-base-future with coin-base-future.

## How to start?
### 1. Install ccxt as first
``` Shell
 pip install ccxt 
```
### 2. Copy this .py file into your workfolder.

### 3. import it in your .py file.
``` Python
  from BinanceFutures import BinanceFut
```
## Examples:
``` Python
from BinanceFutures import BinanceFut
  
if __name__ == '__main__':
    ex = BinanceFut()
    ex.apiKey = ''
    ex.secret = ''
    symbol = 'BTCUSDT'
    print(ex.get_futures_klines(symbol, '1m'))
    print(ex.get_futures_depth(symbol))
    print(ex.get_futures_trades(symbol))
    print(ex.get_futures_balances())
    print(ex.get_futures_positions())
```

## Some tips:
- The SDK wrappered several most frequently used methods not all. The other methods may update sooner.
- The SDK will differ coin-base-futures from usdt-based-futures by symbol name(or param inputted in get position/balance method) automatically. So, make sure your symbol name is correctly inputted.
- Welcom to all business corporation: 
  - Getting invitation/broker rebate. 
  - Learning quantitative trading. 
  - Design program for your strategy. 
  - Project liquidity provider bot.
  - and so on.
- Contact me: 
  - e-mail: 849567264@qq.com
  - Wechat: abcdef20201107
  - Telgram: @lurker123
