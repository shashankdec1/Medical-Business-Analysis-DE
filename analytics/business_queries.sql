
--1 Average sales per year
SELECT year, AVG(sales_value) AS avg_sales
FROM pharma_sales
GROUP BY year;

-- 2 Total sales per hospital
SELECT hospital, SUM(sales_value) AS total_sales
FROM pharma_sales
GROUP BY hospital;

-- 3 Most common treatment
SELECT treatment_type, COUNT(*) AS total
FROM patient_treatments
GROUP BY treatment_type
ORDER BY total DESC;

-- 4 Total treatment cost per year
SELECT year, SUM(treatment_cost) AS total_cost
FROM patient_treatments
GROUP BY year;

-- 5 Hospital performance
SELECT hospital,
SUM(sales_value) AS medicine_sales,
SUM(treatment_cost) AS treatment_revenue
FROM healthcare_merged
GROUP BY hospital;
