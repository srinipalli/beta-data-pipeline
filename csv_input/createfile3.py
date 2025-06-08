import csv

data = [
    {
        "ticketid": "TKT-3001",
        "triage_level": "Critical",
        "modulename": "Login",
        "bug_title": "Multiple failed attempts lock out valid users",
        "bug_desc": "After 3 failed logins, even valid users are locked out without reset options.",
        "priority": "L1",
        "status": "Open",
        "category": "Authentication",
        "datereported": "2023-09-01",
        "assignee": "Aarav Mehta",
        "assignee_date": "2023-09-02",
        "src": "C"
    },
    {
        "ticketid": "TKT-3002",
        "triage_level": "High",
        "modulename": "Cart",
        "bug_title": "Cart items disappear after reload",
        "bug_desc": "When refreshing the cart page, previously added items vanish intermittently.",
        "priority": "L2",
        "status": "In Progress",
        "category": "UX",
        "datereported": "2023-08-12",
        "assignee": "Bella Singh",
        "assignee_date": "2023-08-13",
        "src": "C"
    },
    {
        "ticketid": "TKT-3003",
        "triage_level": "Medium",
        "modulename": "Email",
        "bug_title": "Welcome emails not sent to Gmail addresses",
        "bug_desc": "New Gmail users are not receiving onboarding emails due to SPF/DKIM failure.",
        "priority": "L3",
        "status": "Open",
        "category": "Communication",
        "datereported": "2023-10-05",
        "assignee": "Carlos Ruiz",
        "assignee_date": "2023-10-06",
        "src": "C"
    },
    {
        "ticketid": "TKT-3004",
        "triage_level": "Low",
        "modulename": "Reports",
        "bug_title": "Report names overflow sidebar",
        "bug_desc": "In the analytics panel, long report titles overflow and overlap with the UI.",
        "priority": "L5",
        "status": "Closed",
        "category": "UI",
        "datereported": "2023-07-10",
        "assignee": "Dana Iqbal",
        "assignee_date": "2023-07-11",
        "src": "C"
    },
    {
        "ticketid": "TKT-3005",
        "triage_level": "Medium",
        "modulename": "Admin",
        "bug_title": "Admin panel crashes on bulk user import",
        "bug_desc": "Uploading large CSVs with over 500 users causes memory crash in admin panel.",
        "priority": "L3",
        "status": "Open",
        "category": "Admin Tools",
        "datereported": "2023-06-20",
        "assignee": "Elena Novak",
        "assignee_date": "2023-06-21",
        "src": "C"
    },
    {
        "ticketid": "TKT-3006",
        "triage_level": "Planning",
        "modulename": "Mobile",
        "bug_title": "Dark mode not supported",
        "bug_desc": "Users on iOS and Android request dark mode support for accessibility.",
        "priority": "L4",
        "status": "Planned",
        "category": "Feature Request",
        "datereported": "2023-05-30",
        "assignee": "Fatima Khan",
        "assignee_date": "2023-05-31",
        "src": "C"
    },
    {
        "ticketid": "TKT-3007",
        "triage_level": "Critical",
        "modulename": "Database",
        "bug_title": "Data loss after rollback",
        "bug_desc": "Transactional rollback sometimes leaves tables partially updated or corrupted.",
        "priority": "L1",
        "status": "In Progress",
        "category": "Data Integrity",
        "datereported": "2023-09-15",
        "assignee": "George Tan",
        "assignee_date": "2023-09-16",
        "src": "C"
    },
    {
        "ticketid": "TKT-3008",
        "triage_level": "High",
        "modulename": "Scheduler",
        "bug_title": "Recurring tasks not triggering on Mondays",
        "bug_desc": "Weekly scheduled jobs skip execution on Mondays due to a timezone mismatch.",
        "priority": "L2",
        "status": "Open",
        "category": "Scheduler",
        "datereported": "2023-08-01",
        "assignee": "Hiroshi Yamamoto",
        "assignee_date": "2023-08-02",
        "src": "C"
    }
]

# Write to CSV
with open("csv_input/stage3file.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
