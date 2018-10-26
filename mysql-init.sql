create database apache_logs;
use apache_logs;
create table sqs (
    id bigint not null auto_increment primary key,
    host varchar(20),
    user varchar(20),
    method varchar(10),
    path varchar(400),
    code int,
    size varchar(100),
    referer varchar(400),
    agent varchar(400),
    ts timestamp,
    dedup_hash varchar(400) not null
);

DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
FLUSH PRIVILEGES;

