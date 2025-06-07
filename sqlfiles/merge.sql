USE ticket;

LOAD DATA LOCAL INFILE '/Users/mbas/Desktop/Tsummarizze/TicketSummary4/TicketSummary/csv_input/Ht2.csv'
INTO TABLE stage1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(ticket_id, severity, module, title, description, priority, status, category, reported_date, assigned_to, assigned_date);

LOAD DATA LOCAL INFILE '/Users/mbas/Desktop/Tsummarizze/TicketSummary4/TicketSummary/csv_input/Ht3.csv'
INTO TABLE stage2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(bug_id, triage, module, title, description, severity, status, category, reported_date, assigned_to, assigned_date);

INSERT IGNORE INTO main_table(
    ticket_id,
    severity,
    module,
    title,
    description,
    priority,
    status,
    category,
    reported_date,
    assigned_to,
    assigned_date
)
SELECT
    ticket_id AS ticket_id,
    severity AS severity,
    module AS module,
    title AS title,
    description AS description,
    priority AS priority,
    status AS status,
    category AS category,
    reported_date AS reported_date,
    assigned_to AS assigned_to,
    assigned_date AS assigned_date
FROM stage1

UNION ALL

SELECT
    bug_id AS ticket_id,
    triage AS severity,
    module AS module,
    title AS title,
    description AS description,
    severity AS priority,
    status AS status,
    category AS category,
    reported_date AS reported_date,
    assigned_to AS assigned_to,
    assigned_date AS assigned_date
FROM stage2;