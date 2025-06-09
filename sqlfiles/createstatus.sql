use ticket;

CREATE TABLE IF NOT EXISTS ticketstatus(
    ticket_id VARCHAR(20) PRIMARY KEY,
    queue CHAR(1)
);