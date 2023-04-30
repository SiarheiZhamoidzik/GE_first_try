import great_expectations as gx
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.core.yaml_handler import YAMLHandler
from great_expectations.profile.user_configurable_profiler import (
    UserConfigurableProfiler,
)

yaml = YAMLHandler()
context = gx.get_context()

# Batch Request to identify the Batch of data that you'll use to validate your Expectations
sql_query = "SELECT ProductID, Name, ProductNumber, MakeFlag, FinishedGoodsFlag, Color, SafetyStockLevel, " \
            "       ReorderPoint, StandardCost, ListPrice, Size " \
            "FROM Production.Product"

batch_request = RuntimeBatchRequest(
    datasource_name="localhost_mssql_db",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="Product_tbl",  # this can be anything that identifies this data
    runtime_parameters={"query": sql_query},
    batch_identifiers={"default_identifier_name": "default_identifier"},
)
context.add_or_update_expectation_suite(expectation_suite_name="initial_state_suite")

# Validator to interactively create our Expectations
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="initial_state_suite"
)

# Validator to create an Expectation based on current state of Production.Product
profiler = UserConfigurableProfiler(profile_dataset=validator)
suite = profiler.build_suite()
context.update_expectation_suite(suite)

# context.build_data_docs() # create docs/

