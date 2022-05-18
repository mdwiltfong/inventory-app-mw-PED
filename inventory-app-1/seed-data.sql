
DELETE FROM items;
DELETE FROM warehouses;
DELETE FROM items_warehouses;
UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'items';

INSERT INTO items (name,price,quantity,sku,deleted)
    VALUES 
  ("Shirt",12.45,134,123456,"false"),
  ("Record",4.85,233,123457,"false"),
  ("Canned Meats",8.62,233,123458,"true");

INSERT INTO warehouses(name)
values
("Lovefield"),
("Ottawa"),
("Las Vegas");

INSERT INTO items_warehouses(item_id,warehouse_id,quantity)
VALUES
(1,1,20),
(1,2,40),
(2,3,50);
