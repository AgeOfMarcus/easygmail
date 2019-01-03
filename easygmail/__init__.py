import imaplib, smtplib

version = "0.0.1"

class LoginException(BaseException):
	pass

class Gmail(object):
	def __init__(self, user_email, user_password):
		self.imap = imaplib.IMAP4_SSL("imap.gmail.com",993)
		try:
			self.imap.login(user_email, user_password)
		except Exception as e:
			raise LoginException(str(e))
		
