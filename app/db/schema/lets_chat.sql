create table users(
    id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    first_name varchar(100) DEFAULT NULL,
    last_name varchar(100) DEFAULT NULL,
    user_name varchar(100) DEFAULT NULL,
    email varchar(100) DEFAULT NULL,
    password varchar(320) DEFAULT NULL,
    status varchar(100) DEFAULT NULL,
    PRIMARY KEY (id)
);