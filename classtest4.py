class UserData(object):
	"""docstring for UserData"""
	def __init__(self, user_id,name):
		self.id = user_id
		self._name = name
		
	def __repr__(self):
		return "ID:{} Name:{}".format(self.id, self.name)

class NewUser(UserData):
	group = 'shiyanlou-louplus'
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		if len(value) > 3 :
			self._name = value
		else:
			print('ERROR')

	@classmethod
	def get_group(cls):
		return cls.group
	@staticmethod
	def format_userdada(id,name):
		return("{}'s id is {}".format(name,id))

			
if __name__ == '__main__':
	user1 = NewUser(101,'jack')
	user1.name = 'Lou'
	user1.name = 'jackie'
	user2 = NewUser(102,'Louplus')
	print(user1.name)
	print(user2.name)	
		
