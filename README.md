# quoinex-client

[![PyPI version](https://badge.fury.io/py/quoinex-client.svg)](https://badge.fury.io/py/quoinex-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

quoinex-client is a python client (sync/async) library for quoinex api

## Installation

    $ pip install quoinex-client

## Usage

```python
#
# sync
#
from quoinex_client.sync import Client

client = Clinet(public_key='your api key', private_key='your api secret')
response = client.get_products()
print(response.status_code, response.json())

#
# async
#
import grequests
from quoinex_client.async import Async

client = Async(public_key='your api key', private_key='your api secret')
reqs = [client.get_products(), client.get_product(id=1), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())


client.get_products() # GET /products
client.get_product(id=1) # GET /products/:id
client.get_order_book(id=1) # GET /products/:id/price_levels
client.get_executions(product_id=1) # GET /executions?product_id=1&limit=2&page=2
client.get_executions(currency_pair_code='BTCJPY',timestamp=1526012797) # GET /executions?product_id=1&timestamp=1430630863&limit=2
client.get_interest_rate_ladder(currency='USD') # GET /ir_ladders/USD
client.create_order(order_type='limit', product_id=1, side='sell', quantity=0.01, price=500.0) # POST /orders
client.get_order(id=1) # GET /orders/:id
client.get_orders() # GET /orders?funding_currency=:currency&product_id=:product_id&status=:status&with_details=1
client.cancel_order(id=1) # PUT /orders/:id/cancel
client.edit_live_order(id=1) # PUT /orders/:id
client.get_order_trades(id=1) # GET /orders/:id/trades
client.get_your_executions(product_id=1) # GET /executions/me?product_id=:product_id
client.get_fiat_accounts() # GET /fiat_accounts
client.create_fiat_account(currency='USD') # POST /fiat_accounts
client.get_crypto_accounts() # GET /crypto_accounts
client.get_account_balances() # GET /accounts/balance
client.create_loan_bid(quantity=50, currency='USD', rate=0.0002) # POST /loan_bids
client.get_loan_bids(currency='USD') # GET /loan_bids?currency=:currency
client.close_loan_bid(id=1) # PUT /loan_bids/:id/close
client.get_loans(currency='JPY') # GET /loans?currency=JPY
client.update_loan(id=1) # PUT /loans/144825
client.get_trading_accounts() # GET /trading_accounts
client.get_trading_account(id=1) # GET /trading_accounts/:id
client.update_leverage_level(id=1) # PUT /trading_accounts/:id
client.get_trades() # GET /trades?funding_currency=:funding_currency&status=:status
client.close_trade(id=1) # PUT /trades/:id/close
client.close_all_trades() # PUT /trades/close_all
client.update_trade(id=1, stop_loss=300, take_profit=600) # PUT /trades/:id
client.get_trade_loans(id=1) # GET /trades/:id/loans
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request