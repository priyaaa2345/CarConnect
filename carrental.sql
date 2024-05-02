create table Vehicle(
VehicleID int primary key,
make text ,
model varchar(255),
dailyRate float,
status int,
passengerCapacity int,
engineCapacity int,
years int,
);

create table Customer(
customerID int Primary Key,
firstName text ,
lastName text,
email varchar(255),
phoneNumber varchar(255));

create table Lease(
leaseID int Primary Key,
 vehicleID int,
 customerID int,
 startDate date,
 endDate date,
 leasetype text,
 foreign key( vehicleID) references vehicle(vehicleID),
  foreign key( customerID) references Customer(CustomerID),
);

create table Payment(
paymentID int Primary Key,
leaseID int,
paymentDate date,
amount float,
foreign key (leaseID) references Lease(leaseID));

select * from Vehicle;
select * from Customer;
select * from Lease;
select * from Payment;

insert into Vehicle values 
(1, 'Toyota', 'Camry','2023-01-05' ,50.00, 1, 4 ,1450,2022),
(2, 'Honda', 'Civic', '2023-01-05',45.00, 1, 7, 1500,2023),
(3 ,'Ford ','Focus'  ,'2023-01-05',48.00 ,0 ,4 ,1400,2022),
(4 ,'Nissan', 'Altima','2023-01-05', 52.00, 1,7,1200,2023),
(5 ,'Chevrolet ','Malibu ' ,'2023-01-05',47.00 ,1 ,4 ,1800,2022),
(6 ,'Hyundai', 'Sonata', '2023-01-05',49.00, 0 ,7, 1400,2023),
(7 ,'BMW 3' ,'Series'  ,'2023-01-05',60.00 ,1 ,7 ,249,2023),
(8, 'Mercedes', 'C-Class','2023-01-05', 58.00, 1 ,8, 2599,2022),
(9 ,'Audi' ,'A4'  ,'2023-01-05',55.00 ,0 ,4 ,2500,2022),
(10 ,'Lexus', 'ES' , '2023-01-05',54.00, 1, 4, 2500,2023);

insert into Customer values
(1, 'John', 'Doe', 'johndoe@example.com', 555-555-5555),
(2 ,'Jane',' Smith' ,'janesmith@example.com', 555-123-4567),
(3 ,'Robert ','Johnson' ,'robert@example.com ',555-789-1234),
(4 ,'Sarah', 'Brown', 'sarah@example.com', 555-456-7890),
(5 ,'David' ,'Lee' ,'david@example.com' ,555-987-6543),
(6, 'Laura', 'Hall', 'laura@example.com', 555-234-5678),
(7 ,'Michael' ,'Davis' ,'michael@example.com', 555-876-5432),
(8, 'Emma' ,'Wilson', 'emma@example.com', 555-432-1098),
(9 ,'William' ,'Taylor', 'william@example.com' ,555-321-6547),
(10, 'Olivia', 'Adams' ,'olivia@example.com', 555-765-4321
);

insert into Lease values
(1, 1, 1, '2023-01-01', '2023-01-05', 'Daily'),
(2 ,2 ,2 ,'2023-02-15' ,'2023-02-28 ','Monthly'),
(3, 3, 3, '2023-03-10 ','2023-03-15', 'Daily'),
(4 ,4 ,4, '2023-04-20' ,'2023-04-30',' Monthly'),
(5 ,5 ,5 ,'2023-05-05', '2023-05-10' ,'Daily'),
(6 ,4 ,3 ,'2023-06-15' ,'2023-06-30',' Monthly'),
(7 ,7 ,7, '2023-07-01', '2023-07-10', 'Daily'),
(8 ,8 ,8 ,'2023-08-12' ,'2023-08-15', 'Monthly'),
(9 ,3 ,3, '2023-09-07' ,'2023-09-10' ,'Daily'),
(10 ,10, 10 ,'2023-10-10' ,'2023-10-31' ,'Monthly');

insert into Payment values
(1, 1, '2023-01-03', 200.00),
(2 ,2 ,'2023-02-20' ,1000.00),
(3 ,3, '2023-03-12' ,75.00),
(4 ,4 ,'2023-04-25 ',900.00),
(5 ,5, '2023-05-07' ,60.00),
(6 ,6, '2023-06-18 ',1200.00),
(7 ,7, '2023-07-03', 40.00),
(8 ,8 ,'2023-08-14' ,1100.00),
(9, 9, '2023-09-09', 80.00),
(10, 10 ,'2023-10-25' ,1500.00);

--1. Update the daily rate for a Mercedes car to 68.

update Vehicle
set dailyrate= 68
where make like 'Mercedes';

--2. Delete a specific customer and all associated leases and payments.

delete from Payment
where leaseID = 3;
delete from Lease
where leaseid=3;
delete from Customer
where customerID= 3;


--3. Rename the "paymentDate" column in the Payment table to "transactionDate".

select paymentdate as transactionDate from payment;

--4. Find a specific customer by email.

select * from customer
where email like 'sarah@example.com';


--5. Get active leases for a specific customer.

select * from Lease
where customerID= 10;

--6. Find all payments made by a customer with a specific phone number.

select * from payment
left join lease on payment.leaseid = Lease.leaseID
left join Customer on lease.customerID=Customer.customerID
where customer.phoneNumber= '-975';

--7. Calculate the average daily rate of all available cars.

select avg(dailyrate) as av from vehicle
where status=1;

--8. Find the car with the highest daily rate.

select make,dailyrate from vehicle 
where dailyrate in (select  max(dailyrate)from vehicle);

--9. Retrieve all cars leased by a specific customer.

select vehicleid, make from vehicle
where vehicleid in (select vehicleid from lease
where customerid= 7);

-- 10. Find the details of the most recent lease.

select * from lease
order by enddate desc
offset 0 rows
fetch next 1 rows only;

--11. List all payments made in the year 2023.

select * from Payment
where year(paymentdate) = 2023;

--12. Retrieve customers who have not made any payments.

select customerid,firstname from Customer
where customerid  in ( select customerid from lease
left join payment on
lease.leaseid = payment.leaseid
where payment.paymentid is null);


--13. Retrieve Car Details and Their Total Payments.

select * from vehicle
right join lease on
vehicle.VehicleID = lease.vehicleID
right join Payment on
lease.leaseID= Payment.leaseID;


--14. Calculate Total Payments for Each Customer.

select firstname,payment.amount from customer
inner join lease on
Customer.customerID = lease.customerID
inner join payment on Lease.leaseID= Payment.leaseID;

--15. List Car Details for Each Lease.

select * from lease
left join Vehicle
on lease.vehicleid = Vehicle.VehicleID;

--16. Retrieve Details of Active Leases with Customer and Car Information.

select * from lease
right join customer on lease.customerid = customer.customerid
right join vehicle on lease.vehicleid = vehicle.vehicleid
where enddate > '2023-10-10';



--17. Find the Customer Who Has Spent the Most on Leases.

select customer.firstname ,payment.amount from Customer
inner join lease on
Customer.customerID= lease.customerID
inner join payment on 
lease.leaseid = payment.leaseid
where amount in (select max(amount) from Payment);

--18. List All Cars with Their Current Lease Information

select * from lease
left join vehicle on
lease.vehicleID = Vehicle.VehicleID;