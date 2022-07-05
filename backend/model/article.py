class Article:

    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content
    
    def __eq__(self, article):
        self.title == article.title and self.author == article.author
    
    def __repr__(self):
        return f'<Article: {self.author}, {self.title}>'