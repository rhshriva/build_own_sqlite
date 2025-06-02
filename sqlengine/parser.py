import sqlparse
from typing import Dict, Any

class SQLParser:
    def parse(self, sql: str) -> Dict[str, Any]:
        """
        Parses a SQL statement and returns a dict with metadata.
        Supported: INSERT, SELECT, CREATE TABLE (basic forms)
        """
        parsed = sqlparse.parse(sql)[0]
        tokens = [t for t in parsed.tokens if not t.is_whitespace]
        command = tokens[0].value.upper()
        if command == 'INSERT':
            # Example: INSERT INTO users (id, name) VALUES (1, 'Alice')
            table_name = tokens[2].value
            columns = tokens[3].value.strip('()').replace(' ', '').split(',')
            values_token = [t for t in tokens if t.match(sqlparse.tokens.Keyword, 'VALUES')]
            if values_token:
                idx = tokens.index(values_token[0])
                values = tokens[idx+1].value.strip('()').split(',')
                # Remove quotes from string values
                values = [v.strip().strip("'").strip('"') for v in values]
            else:
                values = []
            return {
                'command': 'INSERT',
                'table': table_name,
                'columns': columns,
                'values': values
            }
        elif command == 'SELECT':
            # Example: SELECT id, name FROM users
            select_idx = 0
            from_idx = next(i for i, t in enumerate(tokens) if t.match(sqlparse.tokens.Keyword, 'FROM'))
            columns = tokens[select_idx+1].value.replace(' ', '').split(',')
            table_name = tokens[from_idx+1].value
            return {
                'command': 'SELECT',
                'table': table_name,
                'columns': columns
            }
        elif command == 'CREATE':
            # Example: CREATE TABLE users (id INTEGER, name TEXT)
            table_name = tokens[2].value
            columns_def = tokens[3].value.strip('()')
            columns = []
            for col_def in columns_def.split(','):
                parts = col_def.strip().split()
                if len(parts) == 2:
                    columns.append({'name': parts[0], 'type': parts[1].upper()})
            return {
                'command': 'CREATE TABLE',
                'table': table_name,
                'columns': columns
            }
        else:
            raise NotImplementedError(f"Command '{command}' not supported yet.") 