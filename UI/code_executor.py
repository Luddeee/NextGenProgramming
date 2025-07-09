import sys
from io import StringIO
import contextlib
import logging
import math

def execute_python_code(code: str) -> str:
    """
    Safely execute generated Python code and return the output.
    """
    logging.debug(f"Executing code:\n{code}")
    
    # Capture stdout
    output = StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            
            safe_globals = {
                'math': math,
                '__builtins__': {
                    'print': print,
                    'range': range,
                    'len': len,
                    'sum': sum,
                    'str': str,
                    'int': int,
                    'float': float,
                    'round': round,
                },
            }

            exec(code, safe_globals)

            # Call the solve to execute python code
            result = eval("solve()", safe_globals)
            logging.debug(f"Execution result: {result}")

            # Print the result
            print(result)
    
        # Return the result as a string
        return str(result)
    
    except Exception as e:
        logging.error(f"Error executing code: {str(e)}")
        return f"Error: {str(e)}"
