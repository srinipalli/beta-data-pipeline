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
    ticketid: str
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

def try_validate_schema(df, schema_class, date_formats: dict = None):
    df_copy = df.copy()
    expected_fields = set(schema_class.model_fields.keys())
    df_fields = set(df_copy.columns)

    if expected_fields != df_fields:
        print(f"❌ Column mismatch for {schema_class.__name__}")
        print(f"Expected: {expected_fields}")
        print(f"Found:    {df_fields}")
        return False

    # Preprocess dates with multiple format attempts
    if date_formats:
        for col, primary_fmt in date_formats.items():
            if col in df_copy.columns:
                date_success = False
                for fmt in [primary_fmt, "%m/%d/%Y", "%Y-%m-%d"]:
                    try:
                        df_copy[col] = pd.to_datetime(df_copy[col], format=fmt).dt.date
                        date_success = True
                        break
                    except Exception:
                        continue
                if not date_success:
                    print(f"❌ Date parsing failed for '{col}' with all formats")
                    return False

    # Convert all fields to string where expected type is string
    for col in df_copy.columns:
        if schema_class.model_fields[col].annotation == str:
            df_copy[col] = df_copy[col].astype(str)

    # Try full schema validation
    try:
        for row in df_copy.to_dict(orient="records"):
            schema_class(**row)
        return True
    except ValidationError as ve:
        print(f"❌ ValidationError for schema {schema_class.__name__}: {ve}")
        return False
    
def classify_and_save(csv_path, out_dir="csv_input/"):
    df = pd.read_csv(out_dir + csv_path)

    if try_validate_schema(df, Stage1Ticket, {
        "reported_date": "%d/%m/%Y",
        "assigned_date": "%d/%m/%Y"
    }):
        df.to_csv(
            f'{out_dir}Hstage1file.csv',
            index=False,
            mode='a',
            header=not os.path.exists(f'{out_dir}Hstage1file.csv'),
            quoting = csv.QUOTE_ALL
        )

        print(f"🥳{csv_path} → Stage 1")
        return "stage1"

    elif try_validate_schema(df, Stage2Ticket, {
        "reported_date": "%m/%d/%Y",
        "assigned_date": "%m/%d/%Y"
    }):
        df.to_csv(
            f'{out_dir}Hstage2file.csv',
            index=False,
            mode='a',
            header=not os.path.exists(f'{out_dir}Hstage2file.csv'),
            quoting = csv.QUOTE_ALL
        )
        print(f"😃{csv_path} → Stage 2")
        return "stage2"

    elif try_validate_schema(df, Stage3Ticket, {
        "datereported": "%d/%m/%Y",
        "assignee_date": "%d/%m/%Y"
    }):
        df.to_csv(
            f'{out_dir}Hstage3file.csv',
            index=False,
            mode='a',
            header=not os.path.exists(f'{out_dir}Hstage3file.csv'),
            quoting = csv.QUOTE_ALL
        )
        print(f"😁{csv_path} → Stage 3")
        return "stage3"

    else:
        print(f"😡{csv_path} → No matching schema!")
        return None

csv_files = [
    "fileA.csv", "fileB.csv", "fileC.csv", "fileD.csv", "fileE.csv"
]

for file in csv_files:
    classify_and_save(file)
