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

The `sql/validation/` directory contains executable validation scripts for:

- **Order and payment reconciliation:** identifies orders with no line items, missing payments, or payment totals that do not match the calculated order total.
- **Referential integrity:** checks for orders without customers and order items without their related orders or products.
- **Product inventory validation:** checks that product stock quantities are nonnegative.

Each validation script displays its results and raises a SQL exception if it detects a failure. This allows the same checks to be run manually with `psql` or automatically in CI.

## Automated Testing

The pytest suite contains 20 automated tests:

- 13 negative constraint tests that verify invalid data is rejected.
- 7 database validation tests covering record counts, order totals, payment reconciliation, referential integrity, and inventory.

Local test result: **20 passed, 0 failed.**

## Project Structure

- `.github/workflows/pytest.yml` — GitHub Actions CI
- `sql/schema.sql` — database schema
- `sql/seed_data.sql` — sample records
- `sql/validation/` — executable SQL validation queries
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
7. Run the SQL validation scripts:
   - `psql -h localhost -U advanced_sql_user -d advanced_sql_testing -v ON_ERROR_STOP=1 -f sql/validation/order_reconciliation.sql`
   - `psql -h localhost -U advanced_sql_user -d advanced_sql_testing -v ON_ERROR_STOP=1 -f sql/validation/referential_integrity.sql`
   - `psql -h localhost -U advanced_sql_user -d advanced_sql_testing -v ON_ERROR_STOP=1 -f sql/validation/inventory_validation.sql`
8. Run the tests with `python -m pytest -v`.

## Continuous Integration

GitHub Actions runs on an Ubuntu 24.04 runner and provisions a temporary PostgreSQL 15 service. It installs Python dependencies, applies the schema and seed data, executes all three standalone SQL validation scripts, and runs the 20-test pytest suite on pushes and pull requests targeting `main`.

The first GitHub-hosted workflow run completed successfully. Subsequent runs execute the SQL validations and pytest suite as part of the same CI job.

## Author

Created and maintained by DeMarko Moore.
