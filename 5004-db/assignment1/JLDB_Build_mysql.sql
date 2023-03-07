SET FOREIGN_KEY_CHECKS=0;

	DROP TABLE JL_CUSTOMERS;
	DROP TABLE JL_ORDERS;
	DROP TABLE JL_PUBLISHER;
	DROP TABLE JL_AUTHOR;
	DROP TABLE JL_BOOKS;
	DROP TABLE JL_ORDERITEMS;
	DROP TABLE JL_BOOK_AUTHOR;
	DROP TABLE JL_PROMOTION;
	DROP TABLE JL_ACCTMANAGER;
	DROP TABLE JL_ACCTMANAGER2;

SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE JL_CUSTOMERS
(Customer_id  INT,
LastName VARCHAR(10) NOT NULL,
FirstName VARCHAR(10) NOT NULL,
Address VARCHAR(20),
City VARCHAR(12),
State VARCHAR(2),
Zip VARCHAR(5),
Referred INT,
Region CHAR(2),
  CONSTRAINT JL_CUSTOMERS_customer_id_pk PRIMARY KEY(customer_id));

INSERT INTO JL_CUSTOMERS
VALUES (1001, 'MORALES', 'BONITA', 'P.O. BOX 651', 'EASTPOINT', 'FL', '32328', NULL, 'SE');
INSERT INTO JL_CUSTOMERS
VALUES (1002, 'THOMPSON', 'RYAN', 'P.O. BOX 9835', 'SANTA MONICA', 'CA', '90404', NULL, 'W');
INSERT INTO JL_CUSTOMERS 
VALUES (1003, 'SMITH', 'LEILA', 'P.O. BOX 66', 'TALLAHASSEE', 'FL', '32306', NULL, 'SE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1004, 'PIERSON', 'THOMAS', '69821 SOUTH AVENUE', 'BOISE', 'ID', '83707', NULL, 'NW'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1005, 'GIRARD', 'CINDY', 'P.O. BOX 851', 'SEATTLE', 'WA', '98115', NULL, 'NW'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1006, 'CRUZ', 'MESHIA', '82 DIRT ROAD', 'ALBANY', 'NY', '12211', NULL, 'NE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1007, 'GIANA', 'TAMMY', '9153 MAIN STREET', 'AUSTIN', 'TX', '78710', 1003, 'SW'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1008, 'JONES', 'KENNETH', 'P.O. BOX 137', 'CHEYENNE', 'WY', '82003', NULL, 'N'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1009, 'PEREZ', 'JORGE', 'P.O. BOX 8564', 'BURBANK', 'CA', '91510', 1003, 'W'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1010, 'LUCAS', 'JAKE', '114 EAST SAVANNAH', 'ATLANTA', 'GA', '30314', NULL, 'SE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1011, 'MCGOVERN', 'REESE', 'P.O. BOX 18', 'CHICAGO', 'IL', '60606', NULL, 'N');  
INSERT INTO JL_CUSTOMERS 
VALUES (1012, 'MCKENZIE', 'WILLIAM', 'P.O. BOX 971', 'BOSTON', 'MA', '02110', NULL, 'NE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1013, 'NGUYEN', 'NICHOLAS', '357 WHITE EAGLE AVE.', 'CLERMONT', 'FL', '34711', 1006, 'SE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1014, 'LEE', 'JASMINE', 'P.O. BOX 2947', 'CODY', 'WY', '82414', NULL, 'N'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1015, 'SCHELL', 'STEVE', 'P.O. BOX 677', 'MIAMI', 'FL', '33111', NULL, 'SE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1016, 'DAUM', 'MICHELL', '9851231 LONG ROAD', 'BURBANK', 'CA', '91508', 1010, 'W'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1017, 'NELSON', 'BECCA', 'P.O. BOX 563', 'KALMAZOO', 'MI', '49006', NULL, 'N'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1018, 'MONTIASA', 'GREG', '1008 GRAND AVENUE', 'MACON', 'GA', '31206', NULL, 'SE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1019, 'SMITH', 'JENNIFER', 'P.O. BOX 1151', 'MORRISTOWN', 'NJ', '07962', 1003, 'NE'); 
INSERT INTO JL_CUSTOMERS 
VALUES (1020, 'FALAH', 'KENNETH', 'P.O. BOX 335', 'TRENTON', 'NJ', '08607', NULL, 'NE'); 
 
CREATE TABLE JL_ORDERS 
(Order_id INT, 
Customer_id INT, 
OrderDate DATE NOT NULL, 
ShipDate DATE, 
ShipStreet VARCHAR(18), 
ShipCity VARCHAR(15), 
ShipState VARCHAR(2), 
ShipZip VARCHAR(5),
ShipCost DECIMAL(4,2),
  CONSTRAINT JL_ORDERS_order_id_pk PRIMARY KEY(order_id),
  CONSTRAINT JL_ORDERS_customer_id_fk FOREIGN KEY (customer_id)
    REFERENCES JL_CUSTOMERS(customer_id)); 
 
INSERT INTO JL_ORDERS 
VALUES (1000,1005,'2009-03-31','2009-04-02','1201 ORANGE AVE', 'SEATTLE', 'WA', '98114' , 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1001,1010,'2009-03-31','2009-04-01', '114 EAST SAVANNAH', 'ATLANTA', 'GA', '30314', 3.00); 
INSERT INTO JL_ORDERS 
VALUES (1002,1011,'2009-03-31','2009-04-01','58 TILA CIRCLE', 'CHICAGO', 'IL', '60605', 3.00); 
INSERT INTO JL_ORDERS 
VALUES (1003,1001,'2009-04-01','2009-04-01','958 MAGNOLIA LANE', 'EASTPOINT', 'FL', '32328', 4.00); 
INSERT INTO JL_ORDERS 
VALUES (1004,1020,'2009-04-01','2009-04-05','561 ROUNDABOUT WAY', 'TRENTON', 'NJ', '08601', NULL); 
INSERT INTO JL_ORDERS 
VALUES (1005,1018,'2009-04-01','2009-04-02', '1008 GRAND AVENUE', 'MACON', 'GA', '31206', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1006,1003,'2009-04-01','2009-04-02','558A CAPITOL HWY.', 'TALLAHASSEE', 'FL', '32307', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1007,1007,'2009-04-02','2009-04-04', '9153 MAIN STREET', 'AUSTIN', 'TX', '78710', 7.00); 
INSERT INTO JL_ORDERS 
VALUES (1008,1004,'2009-04-02','2009-04-03', '69821 SOUTH AVENUE', 'BOISE', 'ID', '83707', 3.00); 
INSERT INTO JL_ORDERS 
VALUES (1009,1005,'2009-04-03','2009-04-05','9 LIGHTENING RD.', 'SEATTLE', 'WA', '98110', NULL); 
INSERT INTO JL_ORDERS 
VALUES (1010,1019,'2009-04-03','2009-04-04','384 WRONG WAY HOME', 'MORRISTOWN', 'NJ', '07960', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1011,1010,'2009-04-03','2009-04-05', '102 WEST LAFAYETTE', 'ATLANTA', 'GA', '30311', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1012,1017,'2009-04-03',NULL,'1295 WINDY AVENUE', 'KALMAZOO', 'MI', '49002', 6.00); 
INSERT INTO JL_ORDERS 
VALUES (1013,1014,'2009-04-03','2009-04-04','7618 MOUNTAIN RD.', 'CODY', 'WY', '82414', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1014,1007,'2009-04-04','2009-04-05', '9153 MAIN STREET', 'AUSTIN', 'TX', '78710', 3.00); 
INSERT INTO JL_ORDERS 
VALUES (1015,1020,'2009-04-04',NULL,'557 GLITTER ST.', 'TRENTON', 'NJ', '08606', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1016,1003,'2009-04-04',NULL,'9901 SEMINOLE WAY', 'TALLAHASSEE', 'FL', '32307', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1017,1015,'2009-04-04','2009-04-05','887 HOT ASPHALT ST', 'MIAMI', 'FL', '33112', 3.00); 
INSERT INTO JL_ORDERS 
VALUES (1018,1001,'2009-04-05',NULL,'95812 HIGHWAY 98', 'EASTPOINT', 'FL', '32328', NULL); 
INSERT INTO JL_ORDERS 
VALUES (1019,1018,'2009-04-05',NULL, '1008 GRAND AVENUE', 'MACON', 'GA', '31206', 2.00); 
INSERT INTO JL_ORDERS 
VALUES (1020,1008,'2009-04-05',NULL,'195 JAMISON LANE', 'CHEYENNE', 'WY', '82003', 2.00); 
 
CREATE TABLE JL_PUBLISHER 
(PubID INT, 
Name VARCHAR(23), 
Contact VARCHAR(15), 
Phone VARCHAR(12),
  CONSTRAINT JL_PUBLISHER_pubid_pk PRIMARY KEY(pubid)); 
 
INSERT INTO JL_PUBLISHER 
VALUES(1,'PRINTING IS US','TOMMIE SEYMOUR','000-714-8321'); 
INSERT INTO JL_PUBLISHER 
VALUES(2,'PUBLISH OUR WAY','JANE TOMLIN','010-410-0010'); 
INSERT INTO JL_PUBLISHER 
VALUES(3,'AMERICAN PUBLISHING','DAVID DAVIDSON','800-555-1211'); 
INSERT INTO JL_PUBLISHER 
VALUES(4,'READING MATERIALS INC.','RENEE SMITH','800-555-9743'); 
INSERT INTO JL_PUBLISHER 
VALUES(5,'REED-N-RITE','SEBASTIAN JONES','800-555-8284'); 
 
CREATE TABLE JL_AUTHOR 
(AUTHORID VARCHAR(4), 
Lname VARCHAR(10), 
Fname VARCHAR(10),
  CONSTRAINT JL_AUTHOR_AUTHORid_pk PRIMARY KEY(AUTHORid)); 
 
INSERT INTO JL_AUTHOR 
VALUES ('S100','SMITH', 'SAM'); 
INSERT INTO JL_AUTHOR 
VALUES ('J100','JONES','JANICE'); 
INSERT INTO JL_AUTHOR 
VALUES ('A100','AUSTIN','JAMES'); 
INSERT INTO JL_AUTHOR 
VALUES ('M100','MARTINEZ','SHEILA'); 
INSERT INTO JL_AUTHOR 
VALUES ('K100','KZOCHSKY','TAMARA'); 
INSERT INTO JL_AUTHOR 
VALUES ('P100','PORTER','LISA'); 
INSERT INTO JL_AUTHOR 
VALUES ('A105','ADAMS','JUAN'); 
INSERT INTO JL_AUTHOR 
VALUES ('B100','BAKER','JACK');  
INSERT INTO JL_AUTHOR 
VALUES ('P105','PETERSON','TINA'); 
INSERT INTO JL_AUTHOR 
VALUES ('W100','WHITE','WILLIAM'); 
INSERT INTO JL_AUTHOR 
VALUES ('W105','WHITE','LISA'); 
INSERT INTO JL_AUTHOR 
VALUES ('R100','ROBINSON','ROBERT'); 
INSERT INTO JL_AUTHOR 
VALUES ('F100','FIELDS','OSCAR'); 
INSERT INTO JL_AUTHOR 
VALUES ('W110','WILKINSON','ANTHONY'); 
 
CREATE TABLE JL_BOOKS 
(ISBN VARCHAR(10), 
Title VARCHAR(30), 
PubDate DATE, 
PubID INT, 
Cost DECIMAL(5,2), 
Retail DECIMAL(5,2), 
Discount DECIMAL(4,2),
Category VARCHAR(12),
  CONSTRAINT JL_BOOKS_isbn_pk PRIMARY KEY(isbn),
  CONSTRAINT JL_BOOKS_pubid_fk FOREIGN KEY (pubid)
    REFERENCES JL_PUBLISHER (pubid)); 
 
INSERT INTO JL_BOOKS 
VALUES ('1059831198','BODYBUILD IN 10 MINUTES A DAY','2005-01-15',4,18.75,30.95, NULL, 'FITNESS'); 
INSERT INTO JL_BOOKS 
VALUES ('0401140733','REVENGE OF MICKEY','2005-12-14',1,14.20,22.00, NULL, 'FAMILY LIFE'); 
INSERT INTO JL_BOOKS 
VALUES ('4981341710','BUILDING A CAR WITH TOOTHPICKS','2006-03-18',2,37.80,59.95, 3.00, 'CHILDREN'); 
INSERT INTO JL_BOOKS 
VALUES ('8843172113','DATABASE IMPLEMENTATION','2003-06-14',3,31.40,55.95, NULL, 'COMPUTER'); 
INSERT INTO JL_BOOKS 
VALUES ('3437212490','COOKING WITH MUSHROOMS','2004-02-02',4,12.50,19.95, NULL, 'COOKING'); 
INSERT INTO JL_BOOKS 
VALUES ('3957136468','HOLY GRAIL OF ORACLE','2005-12-13',3,47.25,75.95, 3.80, 'COMPUTER'); 
INSERT INTO JL_BOOKS 
VALUES ('1915762492','HANDCRANKED COMPUTERS','2005-01-21',3,21.80,25.00, NULL, 'COMPUTER'); 
INSERT INTO JL_BOOKS 
VALUES ('9959789321','E-BUSINESS THE EASY WAY','2006-03-01',2,37.90,54.50, NULL, 'COMPUTER'); 
INSERT INTO JL_BOOKS 
VALUES ('2491748320','PAINLESS CHILD-REARING','2004-07-17',5,48.00,89.95, 4.50, 'FAMILY LIFE'); 
INSERT INTO JL_BOOKS 
VALUES ('0299282519','THE WOK WAY TO COOK','2004-09-11',4,19.00,28.75, NULL, 'COOKING'); 
INSERT INTO JL_BOOKS 
VALUES ('8117949391','BIG BEAR AND LITTLE DOVE','2005-11-08',5,5.32,8.95, NULL, 'CHILDREN'); 
INSERT INTO JL_BOOKS 
VALUES ('0132149871','HOW TO GET FASTER PIZZA','2006-11-11',4,17.85,29.95, 1.50, 'SELF HELP'); 
INSERT INTO JL_BOOKS 
VALUES ('9247381001','HOW TO MANAGE THE MANAGER','2003-05-06',1,15.40,31.95, NULL,  'BUSINESS'); 
INSERT INTO JL_BOOKS 
VALUES ('2147428890','SHORTEST POEMS','2005-05-01',5,21.85,39.95, NULL, 'LITERATURE'); 
 
CREATE TABLE JL_ORDERITEMS 
     ( Order_id INT,
       Item_id INT,
       ISBN VARCHAR(10),
       Quantity INT(3) NOT NULL, 
       PaidEach DECIMAL(5,2) NOT NULL,
       CONSTRAINT JL_ORDERITEMS_pk PRIMARY KEY (order_id, item_id),
       CONSTRAINT JL_ORDERITEMS_order_id_fk FOREIGN KEY (order_id)
             REFERENCES JL_ORDERS (order_id) ,
       CONSTRAINT JL_ORDERITEMS_isbn_fk FOREIGN KEY (isbn)
             REFERENCES JL_BOOKS (isbn));
 
INSERT INTO JL_ORDERITEMS 
VALUES (1000,1,'3437212490',1,19.95);  
INSERT INTO JL_ORDERITEMS 
VALUES (1001,1,'9247381001',1,31.95);  
INSERT INTO JL_ORDERITEMS 
VALUES (1001,2,'2491748320',1,85.45);  
INSERT INTO JL_ORDERITEMS 
VALUES (1002,1,'8843172113',2,55.95);  
INSERT INTO JL_ORDERITEMS 
VALUES (1003,1,'8843172113',1,55.95);  
INSERT INTO JL_ORDERITEMS 
VALUES (1003,2,'1059831198',1,30.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1003,3,'3437212490',1,19.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1004,1,'2491748320',2,85.45); 
INSERT INTO JL_ORDERITEMS 
VALUES (1005,1,'2147428890',1,39.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1006,1,'9959789321',1,54.50); 
INSERT INTO JL_ORDERITEMS 
VALUES (1007,1,'3957136468',3,72.15); 
INSERT INTO JL_ORDERITEMS 
VALUES (1007,2,'9959789321',1,54.50); 
INSERT INTO JL_ORDERITEMS 
VALUES (1007,3,'8117949391',1,8.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1007,4,'8843172113',1,55.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1008,1,'3437212490',2,19.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1009,1,'3437212490',1,19.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1009,2,'0401140733',1,22.00); 
INSERT INTO JL_ORDERITEMS 
VALUES (1010,1,'8843172113',1,55.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1011,1,'2491748320',1,85.45); 
INSERT INTO JL_ORDERITEMS 
VALUES (1012,1,'8117949391',1,8.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1012,2,'1915762492',2,25.00); 
INSERT INTO JL_ORDERITEMS 
VALUES (1012,3,'2491748320',1,85.45); 
INSERT INTO JL_ORDERITEMS 
VALUES (1012,4,'0401140733',1,22.00); 
INSERT INTO JL_ORDERITEMS 
VALUES (1013,1,'8843172113',1,55.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1014,1,'0401140733',2,22.00); 
INSERT INTO JL_ORDERITEMS 
VALUES (1015,1,'3437212490',1,19.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1016,1,'2491748320',1,85.45); 
INSERT INTO JL_ORDERITEMS 
VALUES (1017,1,'8117949391',2,8.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1018,1,'3437212490',1,19.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1018,2,'8843172113',1,55.95); 
INSERT INTO JL_ORDERITEMS 
VALUES (1019,1,'0401140733',1,22.00); 
INSERT INTO JL_ORDERITEMS 
VALUES (1020,1,'3437212490',1,19.95); 
 
CREATE TABLE JL_BOOK_AUTHOR 
(ISBN VARCHAR(10), 
 JL_AUTHORID VARCHAR(4),
  CONSTRAINT JL_BOOK_AUTHOR_pk PRIMARY KEY (isbn, JL_AUTHORid),
  CONSTRAINT JL_BOOK_AUTHOR_isbn_fk FOREIGN KEY (isbn)
             REFERENCES JL_BOOKS (isbn),
  CONSTRAINT JL_BOOK_AUTHOR_AUTHORid_fk FOREIGN KEY (JL_AUTHORid)
             REFERENCES JL_AUTHOR (AUTHORid)); 
 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('1059831198','S100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('1059831198','P100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('0401140733','J100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('4981341710','K100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('8843172113','P105'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('8843172113','A100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('8843172113','A105'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('3437212490','B100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('3957136468','A100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('1915762492','W100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('1915762492','W105'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('9959789321','J100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('2491748320','R100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('2491748320','F100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('2491748320','B100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('0299282519','S100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('8117949391','R100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('0132149871','S100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('9247381001','W100'); 
INSERT INTO JL_BOOK_AUTHOR 
VALUES ('2147428890','W105'); 
 
CREATE TABLE JL_PROMOTION 
(Gift  VARCHAR(15), 
 Minretail DECIMAL(5,2), 
 Maxretail DECIMAL(5,2)); 
 
INSERT into JL_PROMOTION 
 VALUES ('BOOKMARKER', 0, 12); 
INSERT into JL_PROMOTION 
 VALUES ('BOOK LABELS', 12.01, 25); 
INSERT into JL_PROMOTION 
 VALUES ('BOOK COVER', 25.01, 56); 
INSERT into JL_PROMOTION 
 VALUES ('FREE SHIPPING', 56.01, 999.99); 
COMMIT; 

CREATE TABLE JL_ACCTMANAGER
(amid INT PRIMARY KEY,
amfirst VARCHAR(12)  NOT NULL,
amlast VARCHAR(12)  NOT NULL,
amedate DATE,
region CHAR(2) NOT NULL);
 
CREATE TABLE JL_ACCTMANAGER2
(amid CHAR(4),
amfirst VARCHAR(12)  NOT NULL,
amlast VARCHAR(12)  NOT NULL,
amedate DATE,
region CHAR(2),
     CONSTRAINT JL_ACCTMANAGER2_amid_pk PRIMARY KEY (amid));
     

 
 

 