# Customer Migration
Simulating a simple case of data migration
The migration simulation is done in Python, and separately, also in SQL and PL/SQL.

## Explanation:
We have two systems, a current system consisting of a table of customers with 3 properties (ID, Update_date, Location), and an update system where new rows to be updated/inserted/deleted are listed, with an additional column update_flag which specifies how to treat the row (I = insert, U = update, D = delete).
The task is to build a workflow that updates the current system based on the update system, while taking into consideration certain logical rules:

1. the update date for the record in the update system should be more recent than that of the corresponding record in the current system (otherwise, ignore the update record)
1. if there are multiple update records with the same customer ID, only the most recent one should be considered
1. only insert if a record with the same ID does not already exist
1. warning or error messages if a record to be deleted or updated does not exist in the current system
1. Optional rule (not implemented): do not update if the new record has an empty location value

## Data input example (Python):

4

101 01.01.2000 Berlin

102 02.01.2000 London

103 03.01.2000 Moscow

104 04.01.2000 Paris

5

102 04.02.2018 Kiev U

102 05.02.2018 Istanbul U

103 05.02.2018 D

104 31.12.1999 Prague U

105 05.02.2018 Vienna I

## SQL and PL/SQL solution:

The SQL file contains the DDL, DML code, in addition to DQL (SELECT) to verify the content of the tables after the migration. The PL/SQL script contains an anonymous block that performs the migration.

## Result:
Current

101  01.01.2000     Berlin    

102  05.02.2018     Istanbul  

104  04.01.2000     Paris     

105  05.02.2018     Vienna
