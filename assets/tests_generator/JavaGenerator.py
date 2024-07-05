from Generator import Generator

class JavaGenerator(Generator):


    def __init__(self):
        super().__init__( 
                 or_operator='||', 
                 and_operator='&&', 
                 not_operator='!', 
                 true_syntax='true', 
                 false_syntax='false', 
                 title='Test.java', 
                 bottom="\n}")


    def header_content(self, MUT):
        content = ''
        if (MUT.package_name != ''):
            content += "package " + MUT.package_name + ";\n"
        content += "import org.junit.*;\nimport static org.junit.Assert.assertTrue;\n\npublic class "
        content += MUT.class_name + "Test extends " + MUT.class_name + "{\n"
        return content


    def test_content(self, MUT, test_set_name, cont, testset_position):
        content = "\n\t@Test\n\tpublic void " + test_set_name + str(cont) + "() {\n\t\t"
        content += MUT.output_type + " retorno = " + MUT.name + "("

        for x in range(0, len(MUT.params)):
            if (x == 0):
                content += self.generate_param_value(MUT, x, testset_position)
            else:
                content += ", " + self.generate_param_value(MUT, x, testset_position)

        content += ");\n\t\tassertTrue("
        content += self.generate_expected_output(MUT, testset_position)
        content += ");\n\t}\n"
        return content










