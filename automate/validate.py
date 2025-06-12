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

def try_validate_schema(df, schema_class, date_formats : dict = None): 
    df_copy = df.copy()

    # Preprocess date columns using given formats
    if date_formats:
        for col, fmt in date_formats.items():
            if col in df_copy.columns:
                try:
                    df_copy[col] = pd.to_datetime(df_copy[col], format=fmt).dt.date
                except Exception as e:
                    print(f"❌ Date parsing failed for column '{col}' with format '{fmt}': {e}")
                    return False

    try:
        for row in df_copy.to_dict(orient="records"):
            schema_class(**row)
        return True
    except ValidationError as ve:
        #print(ve)
        return False

def classify_and_save(csv_path, out_dir="csv_input/"):
    df = pd.read_csv(out_dir + csv_path)

    if try_validate_schema(df, Stage1Ticket, {
        "reported_date": "%m/%d/%Y",
        "assigned_date": "%m/%d/%Y"
    }):
        df.to_csv(f'{out_dir}stage1file.csv', index=False, mode='a',header=False)
        print(f"{csv_path} → Stage 1 ✅")
        return "stage1"

    elif try_validate_schema(df, Stage2Ticket, {
        "reported_date": "%m/%d/%Y",
        "assigned_date": "%m/%d/%Y"
    }):
        df.to_csv(f'{out_dir}stage2file.csv', index=False, mode='a', header=False)
        print(f"{csv_path} → Stage 2 ✅")
        return "stage2"

    elif try_validate_schema(df, Stage3Ticket, {
        "datereported": "%d/%m/%Y",
        "assignee_date": "%d/%m/%Y"
    }):
        df.to_csv(f'{out_dir}stage3file.csv', index=False, mode='a', header=False)
        print(f"{csv_path} → Stage 3 ✅")
        return "stage3"

    else:
        print(f"❌ {csv_path} → No matching schema!")
        return None

csv_files = [
    "fileA.csv", "fileB.csv", "fileC.csv", "fileD.csv", "fileE.csv"
]

for file in csv_files:
    classify_and_save(file)
