class UserData(object):
	"""docstring for UserData"""
	def __init__(self, user_id,name):
		self.id = user_id
		self.name = name
		
	def __repr__(self):
		return "ID:{} Name:{}".format(self.id, self.name)

if __name__ == '__main__':
	user1 = UserData(101, 'Jack')
	user2 = UserData(102,'Louplus')
	print(user1)
	print(user2)
		