import os
import sys

os.environ['SDL_VIDEODRIVER'] = 'windib'

# Redirect all output to a file
with open('pytest_output_direct.txt', 'w') as f:
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = f
    sys.stderr = f
    
    try:
        print('Script starting...', flush=True)
        
        import pytest
        print('Pytest imported', flush=True)
        
        exit_code = pytest.main(['-v', 'test_minimal.py'])
        print(f'Pytest exit code: {exit_code}', flush=True)
    except Exception as e:
        print(f'Error: {e}', flush=True)
        import traceback
        traceback.print_exc(file=f)
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        f.write('Script completed\n')
