USE ticket2;

CREATE TABLE IF NOT EXISTS metrics(
    ticket_id VARCHAR(20) PRIMARY KEY,
    summarized CHAR(1) DEFAULT 'N',
    vectorized CHAR(1) DEFAULT 'N'
);


