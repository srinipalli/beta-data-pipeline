USE ticket2;

LOAD DATA LOCAL INFILE '/Users/mbas/Desktop/Tsummarizze/DataPipeline/csv_input/Hstage1file.csv'
INTO TABLE stage1
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(ticket_id, severity, module, title, description, priority, status, category, @reported_date, assigned_to, @assigned_date, sourcename)
SET
    reported_date = STR_TO_DATE(@reported_date, '%m/%d/%Y'),
    assigned_date = STR_TO_DATE(@assigned_date, '%m/%d/%Y');

LOAD DATA LOCAL INFILE '/Users/mbas/Desktop/Tsummarizze/DataPipeline/csv_input/Hstage2file.csv'
INTO TABLE stage2
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(bug_id, triage, module, title, description, severity, status, category, @reported_date, assigned_to, @assigned_date, source_name)
SET
    reported_date = STR_TO_DATE(@reported_date, '%m/%d/%Y'),
    assigned_date = STR_TO_DATE(@assigned_date, '%m/%d/%Y');

LOAD DATA LOCAL INFILE '/Users/mbas/Desktop/Tsummarizze/DataPipeline/csv_input/Hstage3file.csv'
INTO TABLE stage3
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(ticketid, triage_level, modulename, bug_title, bug_desc, priority, status, category, @datereported, assignee, @assignee_date, src)
SET
    datereported = STR_TO_DATE(@datereported, '%d/%m/%Y'),
    assignee_date = STR_TO_DATE(@assignee_date, '%d/%m/%Y');

INSERT IGNORE INTO main_table(
    ticket_id,
    severity,
    module,
    title,
    description,
    triage,
    status,
    category,
    reported_date,
    assigned_to,
    assigned_date,
    source
)
SELECT
    ticket_id AS ticket_id,
    severity AS severity,
    module AS module,
    title AS title,
    description AS description,
    priority AS triage,
    status AS status,
    category AS category,
    reported_date AS reported_date,
    assigned_to AS assigned_to,
    assigned_date AS assigned_date,
    sourcename AS source
FROM stage1

UNION ALL

SELECT
    bug_id AS ticket_id,
    triage AS severity,
    module AS module,
    title AS title,
    description AS description,
    severity AS triage,
    status AS status,
    category AS category,
    reported_date AS reported_date,
    assigned_to AS assigned_to,
    assigned_date AS assigned_date,
    source_name AS source
FROM stage2

UNION ALL

SELECT
    ticketid AS ticket_id,
    triage_level AS severity,
    modulename AS module,
    bug_title AS title,
    bug_desc AS description,
    priority as triage,
    status as status,
    category as category,
    datereported as reported_date,
    assignee as assigned_to,
    assignee_date as assigned_date,
    src as source
FROM stage3;

INSERT IGNORE INTO metrics(
    ticket_id
)
SELECT
    ticket_id as ticket_id
FROM main_table;