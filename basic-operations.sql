use ProgammingHero;

CREATE TABLE Student(
	Roll CHAR(4) primary key,
    Name varchar(50),
    Marks double
);

insert into student
(roll, name, marks) values(1, 'Nayeem', 90);
insert into student
(roll, name) values(2, 'Rahim');

set sql_safe_updates = 0;
update student
set name = 'Shaikh Nayeem Uddin'
where roll = 1;
set sql_safe_updates = 1;

set sql_safe_updates = 0;
delete from student where roll = 1;
set sql_safe_updates = 1;

