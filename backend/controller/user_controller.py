from backend.controller.controller import Controller

class User_Controller(Controller):

	def insert_user(self, username, password):
		query_string = "INSERT INTO USER ('username', 'password') VALUES (?, ?);"
		self.database.cud(query_string, [username, password])
	
	def get_all_users(self):
		query_string = "SELECT * FROM USER;"
		return self.database.r_list(query_string)
	
	def get_user_by_username(self, username):
		query_string = "SELECT * FROM USER WHERE username LIKE ?;"
		return self.database.r_item(query_string, [username])

	def get_users_by_article_title(self, article_title):
		query_string = "SELECT * FROM USER JOIN ARTICLE WHERE ARTICLE.title LIKE ? GROUP BY USER.username;"
		return self.database.r_list(query_string, [article_title])

	def update_username(self, current_username, new_username):
		query_string = "UPDATE USER SET username = ? WHERE username LIKE ?;"
		self.database.cud(query_string, [new_username, current_username])

	def update_password(self, username, new_password):
		query_string = "UPDATE USER SET password = ? WHERE username LIKE ?;"
		self.database.cud(query_string, [new_password, username])

	def delete_user(self, username):
		query_string = "DELETE FROM USER WHERE username LIKE ?;"
		self.database.cud(query_string, [username])
	
	def user_exists(self, username, password):
		query_string = "SELECT COUNT(*) as count FROM USER WHERE username LIKE ? AND PASSWORD LIKE ?;"
		return self.database.r_item(query_string, [username, password]).get("count", 0) > 0
	
	def signup(self, username, password):
		if not self.user_exists(username, password):
			self.insert_user(username, password)
			return True
		return False

	def login(self, username, password):
		return self.user_exists(username, password)