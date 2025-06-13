from pydantic import BaseModel, ValidationError
from typing import List
from datetime import date
import pandas as pd
import os
from datetime import datetime
class Stage1Ticket(BaseModel):
    ticket_id: str
    severity: str
    module: str
    title: str
    description: str
    priority: str
    status: str
    category: str
    reported_date: date
    assigned_to: str
    assigned_date: date
    sourcename: str

class Stage2Ticket(BaseModel):
    bug_id: str
    triage: str
    module: str
    title: str
    description: str
    severity: str
    status: str
    category: str
    reported_date: date
    assigned_to: str
    assigned_date: date
    source_name: str

class Stage3Ticket(BaseModel):
    ticketid: int
    triage_level: str
    modulename: str
    bug_title: str
    bug_desc: str
    priority: str
    status: str
    category: str
    datereported: date
    assignee: str
    assignee_date: date
    src: str

def get_schema_fields(schema_class):
    return set(schema_class.__fields__.keys())

def try_validate_schema(df, schema_class, date_formats=None): 
    df_copy = df.copy()

    # Preprocess date columns using given formats
    if date_formats:
        for col, fmt in date_formats.items():
            if col in df_copy.columns:
                try:
                    df_copy[col] = pd.to_datetime(df_copy[col], format=fmt).dt.date
                except Exception as e:
                    return False  # Date parsing failed → not a valid schema

    try:
        for row in df_copy.to_dict(orient="records"):
            schema_class(**row)
        return True
    except ValidationError:
        return False

def classify_and_save(csv_path, out_dir="csv_input/"):
    df = pd.read_csv(out_dir + csv_path)
    df_columns = set(df.columns)

    # Schema definitions with associated date formats
    schemas = [
        {
            "schema": Stage1Ticket,
            "date_formats": {
                "reported_date": "%Y-%m-%d",
                "assigned_date": "%Y-%m-%d"
            },
            "output": "stage1file.csv",
            "label": "Stage 1"
        },
        {
            "schema": Stage2Ticket,
            "date_formats": {
                "reported_date": "%d-%m-%Y",
                "assigned_date": "%d-%m-%Y"
            },
            "output": "stage2file.csv",
            "label": "Stage 2"
        },
        {
            "schema": Stage3Ticket,
            "date_formats": {
                "datereported": "%d-%m-%Y",
                "assignee_date": "%d-%m-%Y"
            },
            "output": "stage3file.csv",
            "label": "Stage 3"
        }
    ]

    for s in schemas:
        schema_fields = get_schema_fields(s["schema"])
        if df_columns == schema_fields:  # Only proceed if exact match
            if try_validate_schema(df, s["schema"], s["date_formats"]):
                df.to_csv(f"{out_dir}{s['output']}", index=False, mode='a', header=False)
                print(f"{csv_path} → {s['label']} ✅")
                return s["label"].lower()
            else:
                print(f"❌ {csv_path} → Column match but date parse failed for {s['label']}")
                return None

    print(f"❌ {csv_path} → No matching schema!")
    return None

csv_files = [
    "hfilea.csv", "hfileb.csv", "hfilec.csv", "hfiled.csv", "hfilee.csv"
]

for file in csv_files:
    classify_and_save(file)
