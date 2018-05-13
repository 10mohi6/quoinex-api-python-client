# coding: utf-8
import grequests
from sync import Client

class Async(Client):

	def _requests_get(self, uri, headers=None, params=None):
		return grequests.get(uri, headers=headers, timeout=self.timeout, params=params)

	def _requests_put(self, uri, headers=None, params=None):
		return grequests.put(uri, headers=headers, timeout=self.timeout, data=params)

	def _requests_post(self, uri, headers=None, params=None):
		return grequests.post(uri, headers=headers, timeout=self.timeout, data=params)
