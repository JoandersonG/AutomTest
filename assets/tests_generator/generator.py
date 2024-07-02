import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from python_generator import generate_tests_python
from java_generator import generate_tests_java


def generate_tests(MUT, file_path='', programing_language = "java"):
    if(programing_language == "python"):
        generate_tests_python(MUT, file_path)
    elif(programing_language == "java"):
        generate_tests_java(MUT, file_path)