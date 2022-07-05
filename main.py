import eel

from backend.controller.article_controller import Article_Controller
from backend.controller.user_controller import User_Controller


eel.init("./frontend", allowed_extensions=[".html", ".css", ".js"])

urls = {
	"start_urls": "index.html"
}




@eel.expose
def get_all_users():
	uc = User_Controller()
	return uc.get_all_users()

@eel.expose
def get_all_articles():
	ac = Article_Controller()
	return ac.get_all_articles()




eel.start("index.html", mode="default", host="192.168.1.24")