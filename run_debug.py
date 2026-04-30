import os
import sys

# Write debug info immediately
with open('pytest_debug.txt', 'w') as f:
    f.write('Script started\n')

os.environ['SDL_VIDEODRIVER'] = 'windib'

with open('pytest_debug.txt', 'a') as f:
    f.write('Environment set\n')

with open('pytest_debug.txt', 'a') as f:
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = f
    sys.stderr = f
    
    try:
        print('Starting all tests...', flush=True)
        f.flush()
        
        print('About to import pytest...', flush=True)
        f.flush()
        
        import pytest
        print('Pytest imported successfully', flush=True)
        f.flush()
        
    except Exception as e:
        print(f'Error during import: {e}', flush=True)
        import traceback
        traceback.print_exc(file=f)
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
