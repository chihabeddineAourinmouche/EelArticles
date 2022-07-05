import { all_articles } from "./components/all_articles_page/all_articles.js";
import { all_users } from "./components/all_users_page/all_users.js";

let display_all_articles = async () => {

	let data = await eel.get_all_articles()();
	window.location.href = "/all_articles.html";
	// all_articles(data, document);
};

let display_all_users = async () => {

	let data = await eel.get_all_users()();
	window.location.href = "/all_users.html";
	// all_users(data, document);
};

document.addEventListener("DOMContentLoaded", () => {
	document.getElementById("all_articles").addEventListener("click", () => {
		display_all_articles();
	});
	document.getElementById("all_users").addEventListener("click", () => {
		display_all_users();
	});
});