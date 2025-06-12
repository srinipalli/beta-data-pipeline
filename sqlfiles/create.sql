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
    assigned_date DATE,
    sourcename TEXT
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
    assigned_date DATE,
    source_name TEXT
);

CREATE TABLE IF NOT EXISTS stage3 (
    ticketid INT PRIMARY KEY,
    triage_level TEXT,
    modulename TEXT,
    bug_title TEXT,
    bug_desc TEXT,
    priority TEXT,
    status TEXT,
    category TEXT,
    datereported DATE,
    assignee TEXT,
    assignee_date DATE,
    src TEXT
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
    assigned_date DATE,
    source TEXT
);


CREATE TABLE IF NOT EXISTS processed(
    ticket_id VARCHAR(20) PRIMARY KEY,
    summary TEXT,
    priority TEXT,
    category TEXT,
    solution TEXT
);

CREATE TABLE IF NOT EXISTS assign(
    ticket_id VARCHAR(20) PRIMARY KEY,
    assigned_id TEXT,
    assigned_date DATE 
);
