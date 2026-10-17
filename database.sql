CREATE DATABASE watch_store;

USE watch_store;

CREATE TABLE users(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(50),
password VARCHAR(50)
);

INSERT INTO users(username,password)
VALUES('admin','123');

CREATE TABLE products(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
price INT,
image VARCHAR(100)
);

INSERT INTO products(name,price,image)
VALUES
('Rolex',50000,'rolex.jpg'),
('Omega',45000,'omega.jpg'),
('Titan',2500,'titan.jpg'),
('Timex',2000,'timex.jpg'),
('Seiko',15000,'seiko.jpg'),
('Citizen',12000,'citizen.jpg'),
('Sonata',1500,'sonata.jpg'),
('FastTrack',2500,'fastrack.jpg'),
('Armani',18000,'armani.jpg'),
('Guess',10000,'guess.jpg'),
('Tommy Hilfiger',7500,'tommy.jpg'),
('Daniel Wellington',9000,'daniel.jpg'),
('Tissot',30000,'tissot.jpg'),
('Rado',60000,'rado.jpg'),
('Longines',40000,'longines.jpg'),
('G-Shock',8500,'gshock.jpg'),
('gq',5500,'gq.jpg'),
('helios',10000,'helios.jpg'),
('kapoor',20000,'kapoor.jpg'),
('sylvi',15000,'sylvi.jpg'),
('Swatch',5000,'swatch.jpg');

CREATE TABLE cart(
id INT PRIMARY KEY AUTO_INCREMENT,
product_id INT
);