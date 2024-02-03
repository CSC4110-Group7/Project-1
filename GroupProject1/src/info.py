info = """Your Database
The ForestDB application is provided to you as a solution to your database needs

Application Organization
The ForestDB application is organized into multiple different tabs.
Each tab encapsulates a group of similar functionalities provided by the application.
The main functionality of the application is contained within the query tab.

The Manage Menu
The manage menu is where you can find operations that affect the entire database, which aren't query-base.
This is where you will load and save databases from csv files. This can be done using the load/save buttons.

The Query Menu
The query menu is where you can perform a variety of database operations.
Here you will be able to insert, update, search, and delete records by any fields and operators you specify.
Every operation available on the query menu can do one or both of the following: select and assign.

Selection
A selection is done by placing the target value on the left, and the value to select by on the right, with
any of the following applicable operators between: =, <, <=, >, >=, @. The @ operator checks if a field is
contained within another, this is useful for checking substrings. A selection can have multiple conditions,
this is done by placing them on different lines. Selections only support ANDing conditions, OR is not yet
supported.

ex.
name=Ryan

ex.
wage>20.0
company@Tim

Assignment
An assignment is similar to a selection, but only supports the -, +, and = operators (where applicable).
It is important to note that some types do not support all the operations. If this is the case, attempting
to use them will simply fail and nothing will happen. An assignment can be performed on the entire database,
or just on a selection

ex.
wage+2

ex.
name=Ryan
email=als.r@gg.com

Insertion
An insertion requires that every value be filled out, and are of the correct types. Values are seperated
by each line. If any entered values are invalid for their respective type, they will be rejected and nothing
will happen.


Example Table: 'name', 'wage', 'email', 'position'

ex.
Ryan
10.0
als.r@goog.com
worker

ex. This example will fail due to not all the fields being filled out
Ryan
also.r@goog.com
worker"""