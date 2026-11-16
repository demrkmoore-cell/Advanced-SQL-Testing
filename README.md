# Advanced SQL Testing

**Author:** DeMarko Moore

A database QA portfolio project demonstrating relational database design, SQL data validation, PostgreSQL constraint testing, and Python-based test automation.

## Project Overview

This project uses a sample e-commerce database built with PostgreSQL. It validates data relationships, checks financial totals, verifies inventory integrity, and tests that invalid records are rejected by database constraints.

## Technology Stack

- PostgreSQL 15
- Python 3.11
- pytest
- psycopg 3
- python-dotenv
- GitHub Actions

## Database Design

The database contains five related tables:

- `customers`
- `products`
- `orders`
- `order_items`
- `payments`

The schema uses primary keys, foreign keys, unique constraints, NOT NULL requirements, and CHECK constraints to enforce data integrity.

## SQL Validation

The `sql/validation/` directory contains queries for:

- Order and payment reconciliation
- Referential integrity checks
- Product inventory validation

## Automated Testing

The pytest suite contains 20 automated tests:

- 13 negative constraint tests that verify invalid data is rejected.
- 7 database validation tests covering record counts, order totals, payment reconciliation, referential integrity, and inventory.

Local test result: **20 passed, 0 failed.**


## Project Structure

- `.github/workflows/pytest.yml` — GitHub Actions CI
- `sql/schema.sql` — database schema
- `sql/seed_data.sql` — sample records
- `sql/validation/` — SQL validation queries
- `tests/` — automated pytest tests
- `.env.example` — database configuration template
- `requirements.txt` — Python dependencies

## Local Setup

1. Create a PostgreSQL database and a user with permission to create tables and run queries.
2. Create and activate a Python virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Copy `.env.example` to `.env` and enter your local database credentials.
5. Apply the schema with `psql -h localhost -U advanced_sql_user -d advanced_sql_testing -f sql/schema.sql`.
6. Load sample data with `psql -h localhost -U advanced_sql_user -d advanced_sql_testing -f sql/seed_data.sql`.
7. Run the tests with `python -m pytest -v`.

## Continuous Integration

GitHub Actions provisions a temporary PostgreSQL 15 service, installs Python dependencies, applies the schema and seed data, and runs the pytest suite on pushes and pull requests targeting `main`.

The workflow is configured; its first GitHub-hosted run is pending.

## Author

Created and maintained by DeMarko Moore.
