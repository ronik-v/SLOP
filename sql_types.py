"""
SQL types for creating a table
See all field descriptions in the __repr__ method
"""


class Varchar:
	def __init__(self, size: int, null_table: bool, primary_key: bool):
		self.size: int = size
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = f'{Varchar.__name__.upper()}({self.size})'
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class Text:
	def __init__(self, null_table: bool, primary_key: bool):
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = Text.__name__.upper()
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class Date:
	def __init__(self, null_table: bool, primary_key: bool):
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = Date.__name__.upper()
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class Serial:
	def __init__(self, null_table: bool, primary_key: bool):
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = Serial.__name__.upper()
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class BigSerial:
	def __init__(self, null_table: bool, primary_key: bool):
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = BigSerial.__name__.upper()
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class Integer:
	def __init__(self, null_table: bool, primary_key: bool):
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = Integer.__name__.upper()
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class Numeric:
	def __init__(self, precision: int, scale: int, null_table: bool, primary_key: bool):
		self.precision = precision if precision <= 131072 else 0
		self.scale = scale if scale <= self.precision else 0
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = f'{Numeric.__name__.upper()}({self.precision}, {self.scale})'
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple


class Point:
	def __init__(self, null_table: bool, primary_key: bool):
		self.null_table: bool = null_table
		self.primary_key: bool = primary_key

	def __repr__(self):
		_tuple = f'{Point.__name__.upper()}'
		if self.null_table:
			_tuple += ' NOT NULL'
		if self.primary_key:
			_tuple += ' PRIMARY KEY'
		return _tuple
