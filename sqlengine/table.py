from typing import List, Tuple, Callable, Optional, Any
import datetime

class Table:
    def __init__(self, columns: List[Tuple[str, str]]) -> None:
        """
        columns: list of (column_name, data_type) tuples, e.g. [('id', 'INTEGER'), ('name', 'TEXT')]
        """
        self.columns: List[Tuple[str, str]] = columns
        self.rows: List[List[Any]] = []

    def insert(self, values: List[Any]) -> None:
        """
        Insert a row into the table. Enforces column count and basic type checking.
        values: list of values, e.g. [1, 'Alice']
        """
        if len(values) != len(self.columns):
            raise ValueError("Column count does not match")
        checked_values = []
        for (col_name, col_type), value in zip(self.columns, values):
            if col_type == 'INTEGER':
                if not isinstance(value, int):
                    raise TypeError(f"Column '{col_name}' expects INTEGER, got {type(value).__name__}")
                checked_values.append(value)
            elif col_type == 'TEXT':
                if not isinstance(value, str):
                    raise TypeError(f"Column '{col_name}' expects TEXT, got {type(value).__name__}")
                checked_values.append(value)
            elif col_type == 'DATE':
                if isinstance(value, datetime.date):
                    checked_values.append(value)
                elif isinstance(value, str):
                    try:
                        checked_values.append(datetime.datetime.strptime(value, "%Y-%m-%d").date())
                    except ValueError:
                        raise TypeError(f"Column '{col_name}' expects DATE in 'YYYY-MM-DD' format, got '{value}'")
                else:
                    raise TypeError(f"Column '{col_name}' expects DATE, got {type(value).__name__}")
            elif col_type == 'FLOAT':
                if not isinstance(value, float):
                    raise TypeError(f"Column '{col_name}' expects FLOAT, got {type(value).__name__}")
                checked_values.append(value)
            elif col_type == 'BOOLEAN':
                if not isinstance(value, bool):
                    raise TypeError(f"Column '{col_name}' expects BOOLEAN, got {type(value).__name__}")
                checked_values.append(value)
            else:
                raise TypeError(f"Unknown column type '{col_type}' for column '{col_name}'")
        self.rows.append(checked_values)

    def select(self, where: Optional[Callable[[List[Any]], bool]] = None) -> List[List[Any]]:
        """
        Select rows from the table. Optionally filter with a 'where' function.
        """
        if where is None:
            return self.rows
        return [row for row in self.rows if where(row)] 