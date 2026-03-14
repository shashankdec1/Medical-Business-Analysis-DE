CREATE TABLE pharma_sales (
sale_id INT,
medicine TEXT,
hospital TEXT,
quantity INT,
sales_value INT,
year INT
);

CREATE TABLE patient_treatments (
patient_id INT,
hospital TEXT,
treatment_type TEXT,
treatment_cost INT,
year INT
);

CREATE TABLE healthcare_merged (
sale_id INT,
medicine TEXT,
hospital TEXT,
quantity INT,
sales_value INT,
year INT,
patient_id INT,
treatment_type TEXT,
treatment_cost INT
);

INSERT INTO pharma_sales (sale_id, medicine, hospital, quantity, sales_value, year) VALUES
(6001,'Paracetamol','Apollo',5,350,2024),
(6002,'Ibuprofen','Fortis',3,250,2024),
(6003,'Aspirin','AIIMS',6,480,2024),
(6004,'Amoxicillin','Manipal',4,320,2024),
(6005,'Metformin','Max',7,560,2024),
(6006,'Paracetamol','Apollo',8,600,2024),
(6007,'Ibuprofen','Fortis',2,180,2024),
(6008,'Aspirin','AIIMS',5,420,2024),
(6009,'Amoxicillin','Manipal',3,240,2024),
(6010,'Metformin','Max',6,500,2024);

INSERT INTO patient_treatments (patient_id, hospital, treatment_type, treatment_cost, year) VALUES
(6001,'Apollo','Consultation',900,2024),
(6002,'Fortis','Surgery',4500,2024),
(6003,'AIIMS','Therapy',1500,2024),
(6004,'Manipal','Emergency',2200,2024),
(6005,'Max','Consultation',800,2024),
(6006,'Apollo','Therapy',1300,2024),
(6007,'Fortis','Consultation',700,2024),
(6008,'AIIMS','Emergency',2100,2024),
(6009,'Manipal','Surgery',5000,2024),
(6010,'Max','Therapy',1600,2024);

CREATE TABLE healthcare_merged (
sale_id INT,
medicine TEXT,
hospital TEXT,
quantity INT,
sales_value INT,
year INT,
patient_id INT,
treatment_type TEXT,
treatment_cost INT
);

ALTER TABLE pharma_sales 
ALTER COLUMN sales_value TYPE BIGINT;

ALTER TABLE patient_treatments 
ALTER COLUMN treatment_cost TYPE BIGINT;

ALTER TABLE healthcare_merged 
ALTER COLUMN sales_value TYPE BIGINT;

ALTER TABLE healthcare_merged 
ALTER COLUMN treatment_cost TYPE BIGINT;




SELECT MAX(sale_id) FROM pharma_sales;

SELECT MAX(patient_id) FROM patient_treatments;

SELECT MAX(sale_id) FROM healthcare_merged;


INSERT INTO pharma_sales (sale_id, medicine, hospital, quantity, sales_value, year) VALUES
(6011,'Paracetamol','Apollo',6,420,2024),
(6012,'Ibuprofen','Fortis',4,300,2024),
(6013,'Aspirin','AIIMS',5,380,2024),
(6014,'Amoxicillin','Manipal',3,240,2024),
(6015,'Metformin','Max',7,520,2024),
(6016,'Paracetamol','Apollo',2,150,2024),
(6017,'Ibuprofen','Fortis',8,640,2024),
(6018,'Aspirin','AIIMS',4,310,2024),
(6019,'Amoxicillin','Manipal',6,470,2024),
(6020,'Metformin','Max',5,390,2024);

INSERT INTO patient_treatments (patient_id, hospital, treatment_type, treatment_cost, year) VALUES
(6011,'Apollo','Consultation',850,2024),
(6012,'Fortis','Surgery',4200,2024),
(6013,'AIIMS','Therapy',1400,2024),
(6014,'Manipal','Emergency',2300,2024),
(6015,'Max','Consultation',900,2024),
(6016,'Apollo','Therapy',1350,2024),
(6017,'Fortis','Consultation',750,2024),
(6018,'AIIMS','Emergency',2100,2024),
(6019,'Manipal','Surgery',5100,2024),
(6020,'Max','Therapy',1700,2024);



SELECT * 
FROM healthcare_merged
ORDER BY sale_id ASC
LIMIT 10;

SELECT MIN(sale_id), MAX(sale_id)
FROM healthcare_merged;

SELECT MAX(sale_id) FROM pharma_sales;

SELECT MAX(patient_id) FROM patient_treatments;

SELECT MAX(sale_id) FROM healthcare_merged;

