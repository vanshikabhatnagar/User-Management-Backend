drop table  if EXISTS employee;
create table employee (
empID int auto_increment primary key,
name varchar(30) not null,
email varchar(50) not null,
dob date not null,
doj date not null,
dept varchar(30) not null,
phone varchar(13) not null,
desig varchar(30),
hours int not null,
otime int not null, 
paid int not null,
unpaid int not null,
med int not null,
comp int 
);

drop table if EXISTS investors ;
create table investors (
invID int auto_increment primary key,
name varchar(30) not null,
email varchar(50) not null,
doi date not null,
amt int not null,
per int not null,
validity date not null,
phone varchar(13) not null
);

drop table if EXISTS admin ;
create table admin (
admID int auto_increment primary key,
name varchar(30) not null, 
email varchar(50) not null,
phone varchar(13) not null
);

-- add sample data
insert into employee values (1, "emma", "emma@gmail.com", "2000-01-11", "2010-09-28", "xyz", "9818158703", "hod", 98, 7,0, 10, 5, 0);
insert into employee values (2, "harry", "harry@gmail.com", "2000-01-12", "2010-09-29", "abc", "9818158704", "peon", 107, 15, 10,10,5, 10000);
insert into investors values (1, "robert", "robert@gmail.com", "2011-01-11", 100000, 4, "2029-09-08", "9624745488");
insert into investors values (2, "jane", "jane@gmail.com", "2014-01-11", 200000, 9, "2034-09-08", "9627236468");
insert into admin values (1, "susan", "susan@gmail.com", "9664237485");