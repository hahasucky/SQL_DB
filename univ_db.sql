create table student (
ID  varchar(10) not null,
name  varchar(25) not null,
dept_name varchar(20),
tot_cred  numeric(3,0),
primary key (ID),
foreign key (dept_name) references department
);

create table instructor (
ID varchar(4) not null,
name varchar(25) not null,
dept_name varchar(20),
salary numeric(10,0), /* million dollor maximum */
primary key (ID),
foreign key (dept_name) references department
);

create table department (
dept_name varchar(20) not null,
building varchar(25),
budget numeric(12,0), /* 100 million dollor maximum*/
primary key(dept_name)
);

create table advisor (
s_id varchar(10),
i_id varchar(4),
foreign key (s_id) references student,
foreign key (i_id) references instructor
);

create table course (
course_id varchar(7),
title varchar(45),
dept_name varchar(20),
credits numeric(1,0),
primary key (course_id),
foreign key (dept_name) references department
);

create table prereq (
course_id varchar(7),
prereq_id varchar(7),
foreign key (course_id) references course,
foreign key (prereq_id) references course
);

create table classroom (
building varchar(20),
room_no varchar(5),
capacity decimal(3,0),
primary key (building, room_no)
);

create table time_slot (
time_slot_id varchar(40), 
day varchar(7),
start_time varchar(7),
end_time varchar(7),
primary key (time_slot_id)
);

create table section (
course_id varchar(7),
sec_id varchar(1), /*QQQQQ ??? what is sec id?*/
semester varchar(2),
year decimal(4,0),
building varchar(8),
room_no varchar(20),
time_slot_id varchar(40),
primary key (course_id, sec_id, semester, year),
foreign key (time_slot_id) references time_slot
);

create table teaches (
ID varchar(3),
course_id varchar(7),
sec_id varchar(1),
semester varchar(2),
year decimal(4,0),
foreign key (course_id, sec_id, semester, year) references section,
foreign key (ID) references instructor
);

create table takes (
ID varchar(10),
course_id varchar(7),
sec_id varchar(1),
semester varchar(2),
year decimal(4,0),
grade varchar(2),
foreign key(course_id, sec_id, semester, year) references section,
foreign key(ID) references student
);

/*Create 10 instructor 20 students 5 classes 10sections insts,*/





