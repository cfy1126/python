USE caodb;
SHOW TABLES;
SELECT * FROM product;

INSERT INTO product(name)VALUES('清茶');
INSERT INTO product(name)VALUES('绿茶');
SELECT * FROM product WHERE name='清茶';
EXPLAIN SELECT * FROM product WHERE name='清茶';
EXPLAIN SELECT * FROM product WHERE id=2;
ALTER TABLE product ADD INDEX product_name_index(name);
ALTER TABLE product DROP INDEX product_name_index;

SELECT * FROM variant;
DELETE FROM product WHERE id=6;
SELECT AVG(price) FROM variant;
SELECT MAX(price) FROM variant;
SELECT STD(price) FROM variant;
SELECT AVG(price),MAX(price),STD(price) FROM variant;

SELECT product_id,AVG(price) FROM variant GROUP BY product_id;
SELECT size,AVG(price) FROM variant GROUP BY size;
SELECT * FROM product INNER JOIN variant ON product.id=variant.product_id;
SELECT product.name,AVG(variant.price) FROM product INNER JOIN variant ON product.id=variant.product_id GROUP BY variant.product_id;