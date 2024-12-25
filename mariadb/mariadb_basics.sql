
/*show databases;
/*create DATABASE first_example;
USE first_example;
show tables;

CREATE TABLE person(
    person_id SMALLINT unsigned,
    fname varchar(20),
    lname varchar(20),
    gender enum('M','F', 'Others'),
    birth_date DATE,
    street varchar(30),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    postal_code varchar(20),
    constraint pk_person primary key (person_id)
);
show tables;*/
-- DESCRIBE person;

/*CREATE TABLE favorite_food(
    person_id SMALLINT unsigned,
    food varchar(20),
 
 /*   lname varchar(20),
    gender enum('M','F', 'Others'),
    birth_date DATE,
    street varchar(30),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    postal_code varchar(20),

    constraint pk_favorite_food primary key (person_id, food),
    constraint fk_favorite_food_person_id foreign key (person_id) 
       references person(person_id)
); 
DESCRIBE favorite_food;*/

-- select * FROM information_schema.table_contraints
-- WHERE CONSTRAINT_SCHEMA='first_example';

-- SELECT * FROM information_schema.table_constraints
-- WHERE TABLE_NAME='person';

-- inserindo informações
-- INSERT INTO person 
--     values('1', 'Carolina', 'Silva', 'F', '1972-10-2','rua tal', 'cidade j','RJ','BR','25251-090');

-- INSERT INTO person 
--     values('6', 'Carolina', 'Silva', 'F', '1972-10-2','rua tal', 'cidade j','RJ','BR','25251-090'),
--           ('2', 'Carolina', 'Siantos', 'F', '1972-10-2','rua tal', 'cidade j','RJ','BR','25251-090'),
--           ('3', 'Carolina', 'Siantos', 'F', '1972-10-2','rua tal', 'cidade j','RJ','BR','25251-090'),
--           ('4', 'Carolina', 'Siantos', 'F', '1972-10-2','rua tal', 'cidade j','RJ','BR','25251-090');





SELECT * FROM person;
-- INSERT INTO favorite_food VALUES (1, 'lasanha'),
--     (2,'carne assada'), (3, 'fetuccine');


SELECT * FROM favorite_food;


