import os
from pathlib import Path

import psycopg
import pytest
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


@pytest.fixture
def db_connection():
    connection = psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "advanced_sql_testing"),
        user=os.getenv("DB_USER", "advanced_sql_user"),
        password=os.getenv("DB_PASSWORD"),
    )

    try:
        yield connection
    finally:
        connection.close()
