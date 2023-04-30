@ECHO OFF
call .\my_venv\Scripts\activate

python run_checkpoint.py appropriate_state_checkpoint
PAUSE