Hello!

This is Great Expectations training project.

Project description.

The aim of this project is to try GE functionality on MSSQL AdventureWorks2019 database.

Project structure:
- Folder "great_expectations", expectations, data_docs and validation results. Important files are:
	/great_expectations/checkpoints - checkpoints:
		- appropriate_state_checkpoint.yml 	- checkpoint for comparison with appropriate state requirements for "Production.Product" table.
		- initial_state_checkpoint.yml 		- checkpoint for comparison with initial state requirements for "Production.Product" table.
		Initial state requirements of "Production.Product" table were created automatically, using a profiler. 
	/great_expectations/expectations - expectations:
		- initial_state_suite.json			- requirements for "Production.Product" table, which were created automatically, 
		using a profiler.
		- appropriate_state_suite.json		- requirements for "Production.Product" table to be in appropriate state.
		Actually these are narrowed requirements from initial_state_suite.json.
	/great_expectations/uncommitted/data_docs/local_site/index.html - report with Validation Results and Expectation Suites description.
	Currently 2 runs are passed and last one (comparison with initial state after change of data in Production.Product) is failed.
	/great_expectations/uncommitted/datasource_new.ipynb - .ipynb notebook for setting connection to database.
- validate_current_state.py - executable .py file, which can be executed for rewriting initial_state_suite.json expectation with current
state of columns: ProductID, Name, ProductNumber, MakeFlag, FinishedGoodsFlag, Color, SafetyStockLevel, ReorderPoint, StandardCost, ListPrice, Size 
in  "Production.Product" table.
- create_checkpoints.py 	- executable .py file, which can be executed in case if checkpoints should be changed
- run_checkpoint.py 		- executable .py file, which is executed with parameter defining checkpoint for tests execution.
- compare_ProductionProduct_with_appropriate_state.bat	.bat file, which execute run_checkpoint.py with appropriate_state_checkpoint parameter
to compare current state of data in "Production.Product" with appropriate state, defined in appropriate_state_suite.json.
- compare_ProductionProduct_with_inital_state.bat		.bat file, which execute run_checkpoint.py with initial_state_checkpoint parameter
to compare current state of data in "Production.Product" with initial state of data in the moment of validate_current_state.py execution.

How to use:
- Clone repository to local folder
- In accordance with https://docs.greatexpectations.io/docs/guides/setup/optional_dependencies/sql_databases/how_to_setup_gx_to_work_with_sql_databases
it is needed to run pip install 'great_expectations[mssql]' and set up virtual environment 'my_venv' in root folder of cloned repository. 
Activation of venv happens in .bat files, so it is important to have the same pathes as in .bat files.
- Open file /great_expectations/uncommitted/datasource_new.ipynb and set connection to DB in accordance with instruction. It is needed to change 
credentials to the proper ones and check connection.
- Execute either compare_ProductionProduct_with_inital_state.bat or compare_ProductionProduct_with_appropriate_state.bat and check results in 
report /great_expectations/uncommitted/data_docs/local_site/index.html

Known issues:
- Simple rules, which may not reflect real business requirements to data.
- Structure of .py files and approach to their creation was intuitive, so it may be improper.
- For some reason Overview of Expectation Validation Result can not be opened in some cases by link in index.html Report, despite
actual .html file with overview exists in /uncommitted/data_docs/local_site/validations/initial_state_suite/__none__/ folder.
Link text is not created properly in some cases. 