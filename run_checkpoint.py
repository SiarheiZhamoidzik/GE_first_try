"""
This is a basic generated Great Expectations script that runs a Checkpoint,
which was updated to run specific checkpoint passed as parameter.
"""
import sys
import great_expectations as gx

from great_expectations.checkpoint.types.checkpoint_result import (
    CheckpointResult,  # noqa: TCH001
)

set_checkpoint = f"{sys.argv[1]}"

# set_checkpoint = 'initial_state_checkpoint'
# set_checkpoint = 'appropriate_state_checkpoint'
context = gx.get_context()

result: CheckpointResult = context.run_checkpoint(
    checkpoint_name=set_checkpoint,
    batch_request=None,
    run_name=None,
)

if not result["success"]:
    print("Validation failed!")
    sys.exit(1)

print("Validation succeeded!")
sys.exit(0)
