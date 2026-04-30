import sys
import traceback

try:
    print("Attempting to import pytest...", file=sys.stderr)
    sys.stderr.flush()
    
    with open('pytest_import_debug.txt', 'w') as f:
        f.write("Attempting to import pytest\n")
        f.flush()
    
    import pytest
    
    print("Pytest imported successfully", file=sys.stderr)
    sys.stderr.flush()
    
    with open('pytest_import_debug.txt', 'a') as f:
        f.write(f"Pytest imported: {pytest.__version__}\n")
        
except Exception as e:
    print(f"Error importing pytest: {str(e)}", file=sys.stderr)
    sys.stderr.flush()
    
    with open('pytest_import_debug.txt', 'a') as f:
        f.write(f"Error: {str(e)}\n")
        f.write(traceback.format_exc())
