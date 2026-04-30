import os
import sys

os.environ['SDL_VIDEODRIVER'] = 'windib'

with open('pytest_all_tests.txt', 'w') as f:
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = f
    sys.stderr = f
    
    try:
        print('Starting all tests...', flush=True)
        
        import pytest
        print('Pytest imported', flush=True)
        
        # Try different test files
        test_files = ['test_minimal.py', 'test_discovery.py', 'test_simple.py']
        
        for test_file in test_files:
            print(f'\n\nTesting {test_file}...', flush=True)
            exit_code = pytest.main(['-v', test_file])
            print(f'Exit code: {exit_code}', flush=True)
            
    except Exception as e:
        print(f'Error: {e}', flush=True)
        import traceback
        traceback.print_exc(file=f)
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
