import os
import sys

os.environ['SDL_VIDEODRIVER'] = 'windib'

try:
    import pytest
    exit_code = pytest.main(['-v', 'test_minimal.py'])
    print(f'Pytest exit code: {exit_code}')
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
