--task 1
--Created all tables successfully with given constraints and inserted sample data into them.Code in DBschema.sql file.

--outcomes of the following commands are shown below:
DESC students;
DESC courses;
DESC enrollments;
DESC professors;
DESC departments;

SHOW CREATE TABLE professors;
--task 2 Verify normalization

-- 1NF Analysis
-- All attributes of all the tables are atomic and theres no repeating groups.
-- But hypothetically if a column like 'email' in students / professors table had multiple email addresses stored in a single field, it would violate 1NF. In that case, we would need to create a separate table for emails and establish a relationship with the students/professors table to maintain atomicity.
-- Result: Schema is in 1NF. All columns contain atomic values.

-- 2NF Analysis:
-- All tables use a single-column primary key.Since there are no composite primary keys, partial dependencies cannot exist.
-- Result: Schema is in 2NF. There are no partial dependencies. 

-- 3NF Analysis (Third Normal Form):
-- All non-key attributes depend directly on their table's primary key
-- Result: Schema is in 3NF. There are no transitive dependencies.


--task 3


