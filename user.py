class User:
	def __init__(self, username, role, password):
		self.username = username
		self.password = password
		self.role = role
  
	def get_role(self):
		return self.role

	def set_role(self, role):
		self.role = role
  
	def get_username(self):
		return self.username

	def get_hashed_password(self):
		return self.password
  
