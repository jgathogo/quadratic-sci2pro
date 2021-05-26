import os
import sys
import math

"""
Score: 1 full point. Well done!
Notes:
-------
First of all, your work is correct. I noticed you forked instead of cloning. It's actually
more efficient to clone though there is something to learn from cloning. 

Docstrings: 
- typically, we would write the title on the first line immediately after the first triple quote. By skipping to the next line
we inadvertently add a newline, which will show up in the parsed documentation. 
- There are formal formats that one could follow. These can be parsed by, for example, PyCharm so that when you click the function
name at its point of use and press F1 you will see a bubble with the functions usage - very handy when you have functions in 
different modules. 
- One of the most important tools for documentation is Sphinx, primarily built to handle documentation of Python
objects (see https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#python-signatures). Sphinx can use any 
markup language (Markdown, reStructureText) which it can then convert in HTML, LaTeX etc. Here is how we can improve the docstring to 
use reStructuredText by placing some delimiters on the variables (it uses info field lists defined at 
https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists):

    :param float a: coefficient of x^2
    :param float b: coefficient of x
    :param float c: constant
    :return: both solutions
    :rtype: tuple(float, float)
    
- You correctly identifed that we were missing brackets for each solution. 
Another solution is using / for each dividend i.e. (-b + math.sqrt(discriminant)) / 2 / a

- From next class I'll score each exercise with 10 points for a max of 100 points so we can have some granularity. 
"""

def calculate(a, b, c):
    """
    Solve quadratic equation and return the value of x

    Parameters:
        a (float): Value a, not equal to zero
        b(float): Value b
        c(float): Value c

    Returns:
        float:Returning value

       """
    
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
