from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from bs4 import BeautifulSoup

class EmailParser(object):

	def __init__(self, api_key="oXdxHJjFHJ61EMz", sent_to="football-good.rga48cmj@mailosaur.io", sent_from=""):

		self.server_id = "rga48cmj"
		self.client = MailosaurClient(api_key)
		self.criteria = SearchCriteria()
		self.criteria.sent_to = sent_to

		if sent_from:
			self.criteria.sent_from = sent_from

	def extract_otp(self, html_body):
		dom = BeautifulSoup(html_body, 'html.parser')
		otp = dom.select("td[id*='verificationMsg'] p[class*='otp']")
		otp_text = otp[0].text

		return otp_text
	
	def fetch_message(self):

		message = self.client.messages.get(self.server_id, self.criteria)

		return message