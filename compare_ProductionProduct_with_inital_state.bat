@ECHO OFF
call .\my_venv\Scripts\activate

python run_checkpoint.py initial_state_checkpoint
PAUSE