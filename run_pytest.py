import os
import sys
import traceback

try:
    # Set environment variable
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    # Write debug info
    with open('pytest_runner.txt', 'w') as f:
        f.write(f'Python version: {sys.version}\n')
        f.write(f'Working directory: {os.getcwd()}\n')
        f.write(f'Files in directory: {os.listdir(".")}\n')

    # Try to import pytest
    with open('pytest_runner.txt', 'a') as f:
        f.write('\nImporting pytest...\n')
    
    import pytest
    
    with open('pytest_runner.txt', 'a') as f:
        f.write(f'Pytest imported successfully: {pytest.__version__}\n')

    # Run pytest
    with open('pytest_runner.txt', 'a') as f:
        f.write('Running pytest.main()...\n')
    
    exit_code = pytest.main(['-v', 'test_pong.py', '--tb=short'])

    with open('pytest_runner.txt', 'a') as f:
        f.write(f'\nPytest exit code: {exit_code}\n')
        
except Exception as e:
    with open('pytest_runner.txt', 'w') as f:
        f.write(f'Error: {str(e)}\n')
        f.write(traceback.format_exc())
