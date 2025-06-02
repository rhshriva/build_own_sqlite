# Simple In-Memory SQL Database (SQLite-like)

This project is a minimal in-memory SQL database engine built from scratch in Python. It supports basic SQL operations such as creating tables, inserting data, and querying data, with support for multiple data types and SQL parsing using `sqlparse`.

## Project Structure

```
project_root/
│
├── README.md
├── requirements.txt
├── main.py
├── run_all_tests.py
├── run_all.sh
├── run_test.sh
├── sqlengine/
│   ├── __init__.py
│   ├── database.py
│   ├── table.py
│   ├── parser.py
│   └── executor.py
└── tests/
    ├── __init__.py
    └── test_basic.py
```

- `main.py`: Entry point for running the database interactively or via script.
- `sqlengine/`: Core database engine modules.
  - `database.py`: Manages database and tables.
  - `table.py`: Table data structure and row operations. Supports data types: `INTEGER`, `TEXT`, `DATE`, `FLOAT`, `BOOLEAN`.
  - `parser.py`: Parses SQL statements using `sqlparse` and returns metadata as a dictionary.
  - `executor.py`: Executes parsed SQL commands by calling the appropriate database methods.
- `tests/`: Unit tests for the database engine.
- `run_all.sh`: Script to set up a virtual environment and install dependencies.
- `run_test.sh`: Script to activate the environment and run all tests.
- `run_all_tests.py`: Python script to discover and run all tests in the `tests` directory.

## Features
- In-memory storage of tables and data.
- Basic SQL support: `CREATE TABLE`, `INSERT`, `SELECT` (simple forms).
- Data type enforcement: `INTEGER`, `TEXT`, `DATE` (as `YYYY-MM-DD` or `datetime.date`), `FLOAT`, `BOOLEAN`.
- SQL parsing using the `sqlparse` library.

## Getting Started

1. Install dependencies:
   ```bash
   bash run_all.sh
   ```
2. Run `main.py` to start using the database.
3. See `tests/` for usage examples.

## Running Tests

You can run all tests in the `tests` directory in several ways:

- Using the provided shell script:
  ```bash
  bash run_test.sh
  ```
- Using the Python script:
  ```bash
  python run_all_tests.py
  ```
- Or directly with unittest:
  ```bash
  python -m unittest discover tests
  ```

## Example Usage

```python
from sqlengine.database import Database
from sqlengine.parser import SQLParser
from sqlengine.executor import SQLExecutor

# Initialize components
db = Database()
parser = SQLParser()
executor = SQLExecutor(db)

# Example SQL statements
sql_create = "CREATE TABLE users (id INTEGER, name TEXT, birth DATE, active BOOLEAN)"
sql_insert = "INSERT INTO users (id, name, birth, active) VALUES (1, 'Alice', '1990-01-01', True)"
sql_select = "SELECT id, name FROM users"

# Parse and execute
executor.execute(parser.parse(sql_create))
executor.execute(parser.parse(sql_insert))
rows = executor.execute(parser.parse(sql_select))
print(rows)  # Output: [[1, 'Alice']]
```

## Notes
- The SQL parser currently supports basic forms of `CREATE TABLE`, `INSERT`, and `SELECT`.
- For `DATE` columns, you can use either a `datetime.date` object or a string in `YYYY-MM-DD` format.
- Extend the parser and executor to support more SQL features as needed. 