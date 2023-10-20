"""
Hello module for the vspec-template
-----------------------------------

This is the hello module for the vspec-template.
It does not do much.

For info on writing numpydoc style docstrings, see:
https://numpydoc.readthedocs.io/en/latest/format.html
"""

def _hello():
    """
    Private function to say "Hello, world!"
    
    Private functions like this do not show up in the documentation,
    but they can still be documented for internal use.

    Returns
    -------
    str
        A string to say "Hello, world!"
        
    Notes
    -----
    This is an example of 
    numpydoc style docstrings.
    """
    return "Hello, world!"

def hello():
    """
    Say "Hello, world!"
    
    Prints "Hello, world!" to the screen.
        
    """
    print(_hello())