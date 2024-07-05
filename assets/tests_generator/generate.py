import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from PythonGenerator import PythonGenerator
from JavaGenerator import JavaGenerator
from javascript_generator import generate_tests_javascript


def generate_tests(MUT, file_path='', programing_language = "java"):
    if(programing_language == "python"):
        generator = PythonGenerator()
        generator.generate_tests(MUT, file_path)
    elif(programing_language == "java"):
        generator = JavaGenerator()
        generator.generate_tests(MUT, file_path)
    elif(programing_language == "javascript"):
        generate_tests_javascript(MUT, file_path)