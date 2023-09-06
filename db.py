from create_connection import db_connection


class Table:
	"""
	The main class for creating tables in the database and methods for them
	"""
	table_name: str
	fields: dict

	@classmethod
	def request(cls, sql_request: str) -> None:
		conn = db_connection()
		cur = conn.cursor()
		cur.execute(sql_request)
		conn.commit()
		conn.close()

	@classmethod
	def request_with_response(cls, sql_request: str):
		conn = db_connection()
		cur = conn.cursor()
		cur.execute(sql_request)
		result = cur.fetchall()
		conn.commit()
		conn.close()
		return result

	@classmethod
	def create_table(cls) -> None:
		sql_request = f'CREATE TABLE {cls.table_name}(\n'
		for key, value in zip(cls.fields.keys(), cls.fields.values()):
			sql_request += f'\t{key} {value.__repr__()}'
			sql_request += ',\n'
		sql_request = sql_request[:len(sql_request) - 2]
		sql_request += '\n);'
		cls.request(sql_request)

	@classmethod
	def select_all(cls) -> list[tuple]:
		return cls.request_with_response(f'SELECT * FROM {cls.table_name};')

	@classmethod
	def select_by_fields(cls, fields: list[str]) -> list[tuple]:
		sql_request = 'SELECT '
		for field in fields:
			sql_request += f'{field}, '
		sql_request = sql_request[:len(sql_request) - 2]
		sql_request += f' FROM {cls.table_name};'
		return cls.request_with_response(sql_request)

	@classmethod
	def insert(cls, fields: list[str], values: list[str]) -> None:
		sql_request = f'INSERT INTO {cls.table_name}('
		for field in fields:
			sql_request += f'{field}, '
		sql_request = f'{sql_request[:len(sql_request) - 2]}) VALUES('
		for value in values:
			sql_request += f"'{value}', "
		sql_request = f'{sql_request[:len(sql_request) - 2]});'
		cls.request(sql_request)

	@classmethod
	def clear_table(cls) -> None:
		cls.request(f'TRUNCATE {cls.table_name}')

	@classmethod
	def drop_table(cls) -> None:
		cls.request(f'DROP TABLE {cls.table_name}')

	@classmethod
	def delete_tuple_by_field_value(cls, field: str, value: str) -> None:
		cls.request(f"DELETE FROM {cls.table_name} WHERE {field} = '{value}'")

	@classmethod
	def update(cls, columns: list[str], values: list[str], condition: str) -> None:
		sql_request = f'UPDATE {cls.table_name} SET '
		for column, value in zip(columns, values):
			sql_request += f'{column} = {value}, '
		sql_request = sql_request[:len(sql_request)-2]
		sql_request += f' WHERE {condition};'
		cls.request(sql_request)
