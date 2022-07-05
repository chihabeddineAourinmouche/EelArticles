import { User } from "../../model/user.js";
import { user_component } from "../user/user.js";

let all_users = (data, dom) => {

	for (let row of data) {
		let user = new User(row["username"]);
		let user_comp = user_component(user, dom);
		dom.body.appendChild(user_comp);
	}
	
};

export { all_users };