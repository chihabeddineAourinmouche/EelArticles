"use strict";

let user_component = (user, dom) => {

	let user_bar = dom.createElement("div");
	user_bar.className = "user-info-bar";

	let user_name = dom.createElement("span");
	user_name.className = "user-name";
	user_name.innerHTML = user.username;

	user_bar.appendChild(user_name);

	return user_bar;

};

export { user_component };