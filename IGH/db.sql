DROP DATABASE IF EXISTS IGH_users;
CREATE DATABASE IGH_users;
USE IGH_users;

CREATE TABLE user_info (
    username VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    max_posts INT,
    hash_tags JSON,
    insta_ids JSON,
    sources JSON,
    post_type INT
    );

CREATE TABLE user_login(
    username VARCHAR(20) PRIMARY KEY,
    password VARCHAR(40) NOT NULL
);

INSERT INTO user_info VALUES('saurav9878', 'Saurav Kumar',4,'["food", "trave", "usic", "travesl"]','["suraev","suraev2"]', '["reddit"]',0);
