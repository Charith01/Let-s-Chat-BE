use lets_chat;

DROP TABLE IF EXISTS users;
create table users(
    id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    first_name varchar(100) DEFAULT NULL,
    last_name varchar(100) DEFAULT NULL,
    user_name varchar(100) DEFAULT NULL,
    email varchar(100) DEFAULT NULL,
    password varchar(320) DEFAULT NULL,
    phone_number varchar(15) DEFAULT NULL,
    status varchar(100) DEFAULT NULL,
    created_by varchar(320) DEFAULT NULL,
    created_at bigint(20) DEFAULT (unix_timestamp() * 1000),
    updated_by varchar(320) DEFAULT NULL,
    updated_at bigint(20) DEFAULT NULL,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
