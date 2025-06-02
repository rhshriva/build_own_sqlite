from typing import Dict, Any


class SQLExecutor:
    def __init__(self, database):
        self.database = database

    def execute(self, parsed_sql: Dict[str, Any]) -> Any:
        command = parsed_sql['command']
        if command == 'CREATE TABLE':
            columns = [(col['name'], col['type']) for col in parsed_sql['columns']]
            self.database.create_table(parsed_sql['table'], columns)
        elif command == 'INSERT':
            self.database.insert(parsed_sql['table'], parsed_sql['values'])
        elif command == 'SELECT':
            return self.database.select(parsed_sql['table'])
        else:
            raise NotImplementedError(f"Command {command} not supported.")