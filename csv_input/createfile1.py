import csv

data = [
    {
        "ticket_id": "TCK-1001",
        "severity": "High",
        "module": "Authentication",
        "title": "Login fails with correct credentials",
        "description": "Multiple users are unable to log in even with valid usernames and passwords.",
        "priority": "L1",
        "status": "Open",
        "category": "Authentication",
        "reported_date": "2023-10-01",
        "assigned_to": "Alice Johnson",
        "assigned_date": "2023-10-02",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1002",
        "severity": "Medium",
        "module": "Payment",
        "title": "Delayed payment confirmation",
        "description": "Users report a delay of over 10 minutes in payment confirmation after checkout.",
        "priority": "L2",
        "status": "In Progress",
        "category": "Payment",
        "reported_date": "2023-10-05",
        "assigned_to": "Bob Smith",
        "assigned_date": "2023-10-06",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1003",
        "severity": "Critical",
        "module": "Backend",
        "title": "Data loss during server crash",
        "description": "System crash caused the loss of customer order records from last 24 hours.",
        "priority": "L1",
        "status": "Open",
        "category": "Infrastructure",
        "reported_date": "2023-09-15",
        "assigned_to": "Clara Singh",
        "assigned_date": "2023-09-15",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1004",
        "severity": "Low",
        "module": "UI",
        "title": "Misaligned buttons on dashboard",
        "description": "UI buttons on the admin dashboard appear misaligned on Safari browser.",
        "priority": "L4",
        "status": "Open",
        "category": "UI",
        "reported_date": "2023-09-20",
        "assigned_to": "David Lee",
        "assigned_date": "2023-09-22",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1005",
        "severity": "Medium",
        "module": "Notifications",
        "title": "Email notifications not triggered",
        "description": "Some transactional emails are not being sent after order placement.",
        "priority": "L3",
        "status": "In Progress",
        "category": "Communication",
        "reported_date": "2023-08-12",
        "assigned_to": "Ella Kim",
        "assigned_date": "2023-08-13",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1006",
        "severity": "High",
        "module": "Search",
        "title": "Search results incomplete",
        "description": "Several relevant products are missing from search results for common queries.",
        "priority": "L2",
        "status": "Open",
        "category": "Search",
        "reported_date": "2023-10-10",
        "assigned_to": "Frank Wright",
        "assigned_date": "2023-10-11",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1007",
        "severity": "Planning",
        "module": "Reports",
        "title": "Add export to Excel feature",
        "description": "Users have requested an option to export reports in Excel format.",
        "priority": "L5",
        "status": "Planned",
        "category": "Feature Request",
        "reported_date": "2023-07-01",
        "assigned_to": "Grace Patel",
        "assigned_date": "2023-07-02",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1008",
        "severity": "Low",
        "module": "Authentication",
        "title": "Forgot password link UI broken",
        "description": "The 'Forgot Password?' link doesn't appear properly on mobile devices.",
        "priority": "L4",
        "status": "Open",
        "category": "UI",
        "reported_date": "2023-10-04",
        "assigned_to": "Helen Zhou",
        "assigned_date": "2023-10-05",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1009",
        "severity": "Medium",
        "module": "API",
        "title": "API returns 500 error for invalid payload",
        "description": "Instead of a 400 Bad Request, the API returns a 500 error when payload is malformed.",
        "priority": "L3",
        "status": "In Progress",
        "category": "Backend",
        "reported_date": "2023-09-25",
        "assigned_to": "Ian Thomas",
        "assigned_date": "2023-09-26",
        "source": "A"
    },
    {
        "ticket_id": "TCK-1010",
        "severity": "Critical",
        "module": "Payment",
        "title": "Double payment charged to users",
        "description": "Some users have been charged twice for the same order due to a retry bug.",
        "priority": "L1",
        "status": "Open",
        "category": "Payment",
        "reported_date": "2023-09-30",
        "assigned_to": "Julia Fernandez",
        "assigned_date": "2023-10-01",
        "source": "A"
    }
]

with open("csv_input/stage1file.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
print("done")