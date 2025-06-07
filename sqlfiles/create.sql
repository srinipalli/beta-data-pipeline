USE ticket;

CREATE TABLE IF NOT EXISTS stage1 (
    ticket_id VARCHAR(20) PRIMARY KEY,
    severity TEXT,
    module TEXT,
    title TEXT,
    description TEXT,
    priority TEXT,
    status TEXT,
    category TEXT,
    reported_date DATE,
    assigned_to TEXT,
    assigned_date DATE
);

CREATE TABLE IF NOT EXISTS stage2 (
    bug_id VARCHAR(20) PRIMARY KEY,
    triage TEXT,
    module TEXT,
    title TEXT,
    description TEXT,
    severity TEXT,
    status TEXT,
    category TEXT,
    reported_date DATE,
    assigned_to TEXT,
    assigned_date DATE
);


CREATE TABLE IF NOT EXISTS main_table (
    ticket_id VARCHAR(20) PRIMARY KEY,
    severity TEXT,
    module TEXT,
    title TEXT,
    description TEXT,
    priority TEXT,
    status TEXT,
    category TEXT,
    reported_date DATE,
    assigned_to TEXT,
    assigned_date DATE
);

CREATE TABLE IF NOT EXISTS testprocessed(
    ticket_id VARCHAR(20) PRIMARY KEY,
    summary TEXT,
    priority TEXT,
    category TEXT,
    sub_category TEXT,
    assigned_to TEXT,
    reason TEXT
);