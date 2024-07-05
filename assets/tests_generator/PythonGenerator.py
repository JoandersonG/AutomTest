from Generator import Generator

class PythonGenerator(Generator):


    def __init__(self) -> None:
        self.or_operator = 'or'
        self.and_operator = 'and'
        self.not_operator = 'not'
        self.true_syntax = 'True'
        self.false_syntax = 'False'
        self.title = 'Test.py'
        self.bottom = '\nif __name__ == "__main__":\n\tunittest.main()'


def test_content_python(self, MUT, test_set_name, cont, testset_position): #DONE
    content = "\n\tdef test_" + test_set_name + str(cont) + "(self):\n\t\t"
    content += "retorno = self." + MUT.name + "("

    # TO DO: gerar valores
    for x in range(0, len(MUT.params)):
        if (x == 0):
            content += self.generate_param_value(MUT, x, testset_position)
        else:
            content += ", " + self.generate_param_value(MUT, x, testset_position)

    content += ")\n\t\tself.assertTrue("
    content += self.generate_expected_output(MUT, testset_position)
    content += ")\n"
    return content


def header_content(self,MUT): #Falta importar a classe
    content = ''
    if (MUT.package_name != ''):
        content += "package " + MUT.package_name + ";\n"
    content += "import unittest\n\nclass "
    content += MUT.class_name + "Test(unittest.TestCase," + MUT.class_name + "):\n"
    return content