# coding: utf-8
import requests
import time
import jwt

class Client(object):

	def __init__(self, **kwargs):
		self.origin = kwargs.get('origin', 'https://api.quoine.com')
		self.public_key = kwargs.get('public_key', None)
		if self.public_key is None:
			raise Exception('public_key is absent.')
		self.private_key = kwargs.get('private_key', None)
		if self.private_key is None:
			raise Exception('private_key is absent.')
		self.timeout = kwargs.get('timeout', None)

	def _requests_get(self, uri, headers=None, params=None):
		return requests.get(uri, headers=headers, timeout=self.timeout, params=params)

	def _requests_put(self, uri, headers=None, params=None):
		return requests.put(uri, headers=headers, timeout=self.timeout, data=params)

	def _requests_post(self, uri, headers=None, params=None):
		return requests.post(uri, headers=headers, timeout=self.timeout, data=params)

	def _requests(self, path, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		headers = {		
			'X-Quoine-API-Version': '2',
			'X-Quoine-Auth': self._signature(path),
			'Content-Type': 'application/json'
		}
		if method == 'GET':
			res = self._requests_get(uri, headers=headers, params=params)
		elif method == 'PUT':
			res = self._requests_put(uri, headers=headers, params=params)
		else: #method == 'POST'
			res = self._requests_post(uri, headers=headers, params=params)

		return res

	def _signature(self, path):
		payload = {
			'path': path,
			'nonce': time.time(),
			'token_id': self.public_key
		}
		sign = jwt.encode(payload, self.private_key, 'HS256')

		return sign

	def get_products(self, **kwargs):
		params = kwargs
		path = '/products'

		data = self._requests(path, params=params)

		return data

	def get_product(self, **kwargs):
		params = kwargs
		path = '/products/{0}'.format(params['id'])

		data = self._requests(path, params=params)

		return data

	def get_order_book(self, **kwargs):
		params = kwargs
		path = '/products/{0}/price_levels'.format(params['id'])

		data = self._requests(path, params=params)

		return data

	def get_executions(self, **kwargs):
		params = kwargs
		path = '/executions'

		data = self._requests(path, params=params)

		return data

	def get_interest_rate_ladder(self, **kwargs):
		params = kwargs
		path = '/ir_ladders/{0}'.format(params['currency'])

		data = self._requests(path, params=params)

		return data

	def create_order(self, **kwargs):
		params = kwargs
		path = '/orders'

		data = self._requests(path, method='POST', params=params)

		return data

	def get_order(self, **kwargs):
		params = kwargs
		path = '/orders/{0}'.format(params['id'])

		data = self._requests(path, params=params)

		return data

	def get_orders(self, **kwargs):
		params = kwargs
		path = '/orders'

		data = self._requests(path, params=params)

		return data

	def cancel_order(self, **kwargs):
		params = kwargs
		path = '/orders/{0}/cancel'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def edit_live_order(self, **kwargs):
		params = kwargs
		path = '/orders/{0}'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def get_order_trades(self, **kwargs):
		params = kwargs
		path = '/orders/{0}/trades'.format(params['id'])

		data = self._requests(path, params=params)

		return data

	def get_your_executions(self, **kwargs):
		params = kwargs
		path = '/executions/me'

		data = self._requests(path, params=params)

		return data

	def get_fiat_accounts(self, **kwargs):
		params = kwargs
		path = '/fiat_accounts'

		data = self._requests(path, params=params)

		return data

	def create_fiat_account(self, **kwargs):
		params = kwargs
		path = '/fiat_accounts'

		data = self._requests(path, method='POST', params=params)

		return data

	def get_crypto_accounts(self, **kwargs):
		params = kwargs
		path = '/crypto_accounts'

		data = self._requests(path, params=params)

		return data

	def get_account_balances(self, **kwargs):
		params = kwargs
		path = '/accounts/balance'

		data = self._requests(path, params=params)

		return data

	def create_loan_bid(self, **kwargs):
		params = kwargs
		path = '/loan_bids'

		data = self._requests(path, method='POST', params=params)

		return data

	def get_loan_bids(self, **kwargs):
		params = kwargs
		path = '/loan_bids'

		data = self._requests(path, params=params)

		return data

	def close_loan_bid(self, **kwargs):
		params = kwargs
		path = '/loan_bids/{0}/close'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def get_loans(self, **kwargs):
		params = kwargs
		path = '/loans'

		data = self._requests(path, params=params)

		return data

	def update_loan(self, **kwargs):
		params = kwargs
		path = '/loans/{0}'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def get_trading_accounts(self, **kwargs):
		params = kwargs
		path = '/trading_accounts'

		data = self._requests(path, params=params)

		return data

	def get_trading_account(self, **kwargs):
		params = kwargs
		path = '/trading_accounts/{0}'.format(params['id'])

		data = self._requests(path, params=params)

		return data

	def update_leverage_level(self, **kwargs):
		params = kwargs
		path = '/trading_accounts/{0}'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def get_trades(self, **kwargs):
		params = kwargs
		path = '/trades'

		data = self._requests(path, params=params)

		return data

	def close_trade(self, **kwargs):
		params = kwargs
		path = '/trades/{0}/close'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def close_all_trades(self, **kwargs):
		params = kwargs
		path = '/trades/close_all'

		data = self._requests(path, method='PUT', params=params)

		return data

	def update_trade(self, **kwargs):
		params = kwargs
		path = '/trades/{0}'.format(params['id'])

		data = self._requests(path, method='PUT', params=params)

		return data

	def get_trade_loans(self, **kwargs):
		params = kwargs
		path = '/trades/{0}/loans'.format(params['id'])

		data = self._requests(path, params=params)

		return data
