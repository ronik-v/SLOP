# Small lightweight orm for Python (SLOP)
<div class="wrapper">
    <p>A simple and fast orm for postgresql designed to quickly create and edit data</p>
    <div>
        <h3>Technologies</h3>
        <div class="points">
            <ul>
                <li>Python 3.8+</li>
                <li>PostgreSQL 15+</li>
                <li>Driver - psycopg2</li>
            </ul>
        </div>
    </div>
	<div class="start">
		<h3>To start</h3>
		<p>Add all the necessary information to the config and also create a database whose name is also written in the config file</p><br>
	</div>
    <div class="examples">
        <h3>Examples</h3>
        <ul>
            <li>
                <h4>Initialization and creating tables</h4>
                <pre>from SLOP.sql_types import Varchar, Date, BigSerial, Text
from SLOP.db import Table


class Employee(Table):
		table_name = 'Employee'
		fields: dict = {
			'id': BigSerial(null_table=True, primary_key=True),
			'name': Varchar(size=30, null_table=True, primary_key=False),
			'dob': Date(null_table=True, primary_key=False),
			'bio': Text(null_table=False, primary_key=False)
		}</pre>
            <pre>Employee.create_table()</pre>
            </li>
			<li>
				<h4>Adding data to a table</h4>
				<pre>Employee.insert(fields=['name', 'dob', 'bio'], values=['Petry', '1983-06-02', 'some_bio'])
Employee.insert(fields=['name', 'dob', 'bio'], values=['Inga', '1998-02-14', 'some_bio'])
Employee.insert(fields=['name', 'dob', 'bio'], values=['Kate', '2002-01-09', 'some_bio'])</pre>
			</li>
			<li>
				<h5>Get all data from table</h5>
				<pre>data: list[tuple] = Employee.select_all()</pre>
			</li>
			<li>
				<h5>Get data for specific fields</h5>
				<pre>data: list[tuple] = Employee.select_by_fields(fields=['name', 'dob'])</pre>
			</li>
			<li>
				<h5>Delete entry from database</h5>
				<pre>Employee.delete_tuple_by_field_value(field='name', value='Kate')</pre>
			</li>
			<li>
				<h5>Deleting a table</h5>
				<pre>Employee.drop_table()</pre>
			</li>
			<li>
				<h5>Clearing data from a table</h5>
				<pre>Employee.clear_table()</pre>
			</li>
			<li>
				<h5>Update values in a table</h5>
				<pre>Employee.update(columns=['dob', 'bio'], values=["'2001-02-14'", "'someBio'"], condition="dob = '1998-02-14'")</pre>
			</li>
        </ul>
		<div>
			<h3>License</h3>
			<p>Apache License 2.0, details here <a href="LICENSE">LICENSE</a></p>
		</div>
    </div>
</div>