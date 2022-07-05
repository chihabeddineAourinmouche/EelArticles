"use strict";

let article_component = (article, dom) => {

	let _article = dom.createElement("div");
	_article.className = "article-component";

		let article_info = dom.createElement("div");
		article_info.className = "article-info";

			let author = dom.createElement("span");
			author.className = "author";
			author.innerHTML = article.author;
		
			let title = dom.createElement("span");
			title.className = "title";
			title.innerHTML = article.title;

			article_info.appendChild(title);
			article_info.appendChild(author);
		
		let article_content = document.createElement("p");
		article_content.className = "content";
		article_content.innerHTML = article.content;

		_article.appendChild(article_info);
		_article.appendChild(article_content);

	return _article;

};

export { article_component };