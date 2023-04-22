SHOW DATABASES;
USE caodb;
SHOW TABLES;
CREATE TABLE product(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL DEFAULT 30
);

INSERT INTO product(id, name, price)VALUES(1,'拿铁',50);
INSERT INTO product(id, name, price)VALUES(2,'美式',40);
INSERT INTO product(id, name, price)VALUES(3,'奶茶',50);
INSERT INTO product(name, price)VALUES('绿茶', 30);
INSERT INTO product(name,price)VALUES('奶绿',45);
INSERT INTO product(price)VALUES(50);
INSERT INTO product(name)VALUES('清茶');
alter table product convert to character set utf8;
DROP TABLE product;

SELECT * FROM product;
SELECT id,name FROM product;
SELECT * FROM product WHERE price=45;
SELECT * FROM product WHERE name='清茶';
SELECT * FROM product WHERE price<>40;
SELECT * FROM product WHERE name='拿铁' and price<>40;
SELECt * FROM product WHERE name='清茶' or price=50;
SELECT name,price FROM product WHERE price<>40;

SET SQL_SAFE_UPDATES=0;
UPDATE product SET price=10 WHERE name='奶茶';
UPDATE product SET price=100,name='沔渡清茶' WHERE name='清茶';
UPDATE product SET price=35 WHERE price<=35;
UPDATE product SET price=60;

DELETE FROM product WHERE name='拿铁';
DELETE FROM product;
