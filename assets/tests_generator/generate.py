import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from PythonGenerator import PythonGenerator
from JavaGenerator import JavaGenerator
from JavascriptGenerator import JavascriptGenerator


def generate_tests(MUT, file_path='', programing_language = "java"):
    if(programing_language == "python"):
        generator = PythonGenerator()
    elif(programing_language == "java"):
        generator = JavaGenerator()
    elif(programing_language == "javascript"):
        generator = JavascriptGenerator()
        
    generator.generate_tests(MUT, file_path)