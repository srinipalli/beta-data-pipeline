USE ticket2;
set SQL_SAFE_UPDATES = 0;
DROP TABLE IF EXISTS employee;
CREATE TABLE IF NOT EXISTS employee(
    employee_id VARCHAR(20) PRIMARY KEY,
    employee_name TEXT,
    category TEXT,
    triage CHAR(2),
    role CHAR(1)
);

LOAD DATA LOCAL INFILE '/Users/mbas/Desktop/Tsummarizze/beta-data-pipeline/csv_input/employeetable.csv'
INTO TABLE employee
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(employee_id, employee_name, category, triage, role);

