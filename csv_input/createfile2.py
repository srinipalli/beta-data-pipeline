import csv

data = [
    {
        "bug_id": "BUG-2001",
        "triage": "High",
        "module": "Authentication",
        "title": "OAuth token not refreshing",
        "description": "Access tokens are not getting refreshed automatically after expiry, causing user logouts.",
        "severity": "L1",
        "status": "Open",
        "category": "Security",
        "reported_date": "2023-10-01",
        "assigned_to": "Liam Carter",
        "assigned_date": "2023-10-02",
        "source_name": "B"
    },
    {
        "bug_id": "BUG-2002",
        "triage": "Medium",
        "module": "Search",
        "title": "Filter results ignore date range",
        "description": "When users select a date filter in search, results still include entries outside the range.",
        "severity": "L2",
        "status": "In Progress",
        "category": "Search",
        "reported_date": "2023-09-18",
        "assigned_to": "Nina Kapoor",
        "assigned_date": "2023-09-19",
        "source_name": "B"
    },
    {
        "bug_id": "BUG-2003",
        "triage": "Critical",
        "module": "Payment",
        "title": "Refund process fails intermittently",
        "description": "Some refund attempts timeout or fail to process, especially for international transactions.",
        "severity": "L1",
        "status": "Open",
        "category": "Finance",
        "reported_date": "2023-08-10",
        "assigned_to": "Omar Ali",
        "assigned_date": "2023-08-11",
        "source_name": "B"
    },
    {
        "bug_id": "BUG-2004",
        "triage": "Low",
        "module": "UI",
        "title": "Hover tooltip overlaps buttons",
        "description": "On the dashboard, tooltips obscure nearby buttons making them hard to click.",
        "severity": "L4",
        "status": "Open",
        "category": "UI",
        "reported_date": "2023-07-25",
        "assigned_to": "Priya Verma",
        "assigned_date": "2023-07-26",
        "source_name": "B"
    },
    {
        "bug_id": "BUG-2005",
        "triage": "Planning",
        "module": "Analytics",
        "title": "Add CSV export for usage stats",
        "description": "Users want the ability to export their usage analytics data in CSV format.",
        "severity": "L5",
        "status": "Planned",
        "category": "Feature Request",
        "reported_date": "2023-06-15",
        "assigned_to": "Quentin Huang",
        "assigned_date": "2023-06-16",
        "source_name": "B"
    },
    {
        "bug_id": "BUG-2006",
        "triage": "Medium",
        "module": "Notifications",
        "title": "Push notifications sent twice",
        "description": "Mobile app notifications for events are being sent twice to some users.",
        "severity": "L2",
        "status": "In Progress",
        "category": "Communication",
        "reported_date": "2023-09-02",
        "assigned_to": "Rita Gomez",
        "assigned_date": "2023-09-03",
        "source_name": "B"
    }
]

with open("csv_input/stage2file.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
