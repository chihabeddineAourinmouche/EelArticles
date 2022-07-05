from backend.controller.controller import Controller

class Article_Controller(Controller):

	def insert_article(self, author, title, content):
		query_string = "INSERT INTO ARTICLE ('author', 'title', 'content') VALUES (?, ?, ?);"
		self.database.cud(query_string, [author, title, content])

	def update_article_title(self, author, title, new_title):
		query_string = "UPDATE ARTICLE SET title = ? WHERE author LIKE ? AND title LIKE ?;"
		self.database.cud(query_string, [new_title, author, title])

	def update_article_content(self, author, title, new_content):
		query_string = "UPDATE ARTICLE SET content = ? WHERE author LIKE ? AND title LIKE ?;"
		self.database.cud(query_string, [new_content, author, title])

	def delete_article(self, author, title):
		query_string = "DELETE * FROM ARTICLE WHERE author LIKE ? AND title LIKE ?;"
		self.database.cud(query_string, [author, title])

	def delete_articles_by_author(self, author):
		query_string = "DELETE * FROM ARTICLE WHERE author LIKE ?;"
		self.database.cud(query_string, [author])

	def get_all_articles(self):
		query_string = "SELECT * FROM ARTICLE;"
		return self.database.r_list(query_string)

	def get_article_by_author_and_title(self, author, title):
		query_string = "SELECT * FROM ARTICLE WHERE author LIKE ? AND title LIKE ?;"
		return self.database.r_item(query_string, [author, title])

	def get_articles_by_author(self, author):
		query_string = "SELECT * FROM ARTICLE WHERE author LIKE ?;"
		return self.database.r_list(query_string, [author])

	def get_articles_by_title(self, title):
		query_string = "SELECT * FROM ARTICLE WHERE title LIKE ?;"
		return self.database.r_list(query_string, [title])