import easygui as e
username = e.enterbox ("账号")
userpwd = e.enterbox ("密码")
class User():
	def __init__(self,name,pwd):
		self.name = name
		self.pwd = pwd
	def register(self):
		e.msgbox("账号为"+self.name +"\n" + "密码为"+ self.pwd)
user = User (username,userpwd)
user.register()
u = e.erterbox ('账号')
p = e.enterbox ('密码')
if u == username and p == userpwd:
	print ( '登录成功')
else :
	print ( '登录失败')
