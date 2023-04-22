SHOW DATABASES;
USE caodb;
SHOW TABLES;
CREATE TABLE product(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE variant(
	id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    size VARCHAR(255) NOT NULL,
    price INT NOT NULl DEFAULT 30
);
INSERT INTO product(name)VALUES('美式');
INSERT INTO product(name)VALUES('拿铁');
INSERT INTO product(name)VALUES('奶茶');
INSERT INTO product(name)VALUES('清茶');
SELECT * FROM product;
SELECT * FROM variant;
INSERT INTO variant(product_id,size,price)VALUES(1,'中杯',40);
INSERT INTO variant(product_id,size,price)VALUES(1,'大杯',50);
INSERT INTO variant(product_id,size,price)VALUES(2,'中杯',50);
INSERT INTO variant(product_id,size,price)VALUES(2,'大杯',60);
INSERT INTO variant(product_id,size,price)VALUES(3,'中杯',45);
INSERT INTO variant(product_id,size,price)VALUES(3,'大杯',55);
INSERT INTO variant(product_id,size,price)VALUES(5,'大杯',100);
DROP TABLE variant;
SELECT * FROM product INNER JOIN variant ON product.id=variant.product_id;
SELECT * FROM product LEFT JOIN variant ON product.id=variant.product_id;
SELECT * FROM product RIGHT JOIN variant ON product.id=variant.product_id;
SELECT product.name,variant.size,variant.price FROM product INNER JOIN variant ON product.id=variant.product_id; 
SELECT product.name,variant.size,variant.price FROM product LEFT JOIN variant ON product.id=variant.product_id;
SELECT product.name,variant.size,variant.price FROM product RIGHT JOIN variant ON product.id=variant.product_id;
DELETE FROM variant WHERE id=7;
ALTER TABLE variant ADD FoREIGN KEY(product_id)REFERENCES product(id);
DELETE FROM product WHERE id=3;
