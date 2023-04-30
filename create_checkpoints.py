import validate_current_state
import great_expectations as gx

context = gx.get_context()
batch_request = validate_current_state.batch_request

# Create a Checkpoint
checkpoint = gx.checkpoint.SimpleCheckpoint(
    name="initial_state_checkpoint",
    data_context=context,
    validations=[
        {
            "batch_request": batch_request,
            "expectation_suite_name": "initial_state_suite",
        },
    ],
)
# Save Checkpoint
context.add_or_update_checkpoint(checkpoint=checkpoint)

#  build Data Docs with the latest checkpoint
context.build_data_docs()


# Create a Checkpoint
checkpoint = gx.checkpoint.SimpleCheckpoint(
    name="appropriate_state_checkpoint",
    data_context=context,
    validations=[
        {
            "batch_request": batch_request,
            "expectation_suite_name": "appropriate_state_suite",
        },
    ],
)
# Save your Checkpoint
context.add_or_update_checkpoint(checkpoint=checkpoint)

#  build Data Docs with the latest checkpoint
context.build_data_docs()
