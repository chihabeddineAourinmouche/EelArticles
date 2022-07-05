import { Article } from "../../model/article.js";
import { article_component } from "../article/article.js";

let all_articles = (data, dom) => {

	for (let row of data) {
		let article = new Article(row["author"], row["title"], row["content"]);
		let article_comp = article_component(article, dom);
		dom.body.appendChild(article_comp);
	}
	
};

export { all_articles };