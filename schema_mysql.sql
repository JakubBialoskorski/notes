CREATE TABLE notes (
	id INT NOT NULL AUTO_INCREMENT,
	note_title TEXT(255),
	note TEXT,
	note_markdown TEXT,
	tags TEXT(200),
	user_id INT,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE tags (
	id INT NOT NULL AUTO_INCREMENT,
	tag TEXT,
	user_id INT,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	username TEXT(255),
	password TEXT(200),
	email TEXT(200),
	PRIMARY KEY (id)
);
