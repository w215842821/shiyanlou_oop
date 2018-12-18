class UserData(object):
	"""docstring for UserData"""
	def __init__(self, user_id,name):
		self.id = user_id
		self.name = name
		
	def __repr__(self):
		return "ID:{} Name:{}".format(self.id, self.name)

class NewUser(UserData):
	group = 'shiyanlou-louplus'
	def get_name(self):
		return self.name

	def set_name(self,value):
		self.name = value
	
	@classmethod
	def get_group(cls):
		return cls.group
	@staticmethod
	def format_userdada(id,name):
		return("{}'s id is {}".format(name,id))

			
if __name__ == '__main__':
	print(NewUser.get_group())
	print(NewUser.format_userdada(100,'Lucy'))
	
		