from sqlengine.table import Table
from typing import List, Tuple, Callable, Optional, Any

class Database:
    def __init__(self) -> None:
        self.tables: dict[str, Table] = {}

    def create_table(self, name: str, columns: List[Tuple[str, str]]) -> None:
        """
        columns: list of (column_name, data_type) tuples, e.g. [('id', 'INTEGER'), ('name', 'TEXT')]
        """
        if name in self.tables:
            raise ValueError(f"Table '{name}' already exists.")
        self.tables[name] = Table(columns)

    def insert(self, table_name: str, values: List[Any]) -> None:
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        self.tables[table_name].insert(values)

    def select(self, table_name: str, where: Optional[Callable[[List[Any]], bool]] = None) -> List[List[Any]]:
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        return self.tables[table_name].select(where) 