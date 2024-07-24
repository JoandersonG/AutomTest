from Generator import Generator
import datetime
import random

class PythonGenerator(Generator):


    def __init__(self):
        super().__init__(
                or_operator = 'or',
                and_operator = 'and',
                not_operator = 'not',
                true_syntax = 'True',
                false_syntax = 'False',
                title = 'Test.py',
                bottom = '\nif __name__ == "__main__":\n\tunittest.main()')
    
    def get_date_format(self, year, month, day):
        return f'datetime.date({year}, {month}, {day})'
    

    def generate_date_output(self, v1, v2, v3):
        if (v1 != '' and v2 != ''):
            ymd1 = self.get_YearMonthDay_from_Date(v1)
            ymd2 = self.get_YearMonthDay_from_Date(v2)

            start_date = self.get_date_format(int(ymd1[0]), int(ymd1[1]), int(ymd1[2]))
            end_date = self.get_date_format(int(ymd2[0]), int(ymd2[1]), int(ymd2[2]))

            content = '(retorno >= ' + start_date + " "+ self.and_operator + ' retorno <= ' + end_date + ') '

        if (v3 != ''):
            vals = v3.replace(" ", "").split(';')
            for x in range(0, len(vals)):
                ymd3 = self.get_YearMonthDay_from_Date(vals[x])
                date = self.get_date_format(int(ymd3[0]), int(ymd3[1]), int(ymd3[2]))
                if (content != ''):
                    content += self.or_operator + ' retorno == ' + date
                else:
                    content += 'retorno == ' + date
        return content


    def header_content(self,MUT): #Falta importar a classe
        content = ''
        # if (MUT.package_name != ''):
        #     content += "package " + MUT.package_name + ";\n"
        content += "import unittest\n\nclass "
        content += MUT.class_name + "Test(unittest.TestCase," + MUT.class_name + "):\n"
        return content


    def test_content(self, MUT, test_set_name, cont, testset_position): #DONE
        content = "\n\tdef test_" + test_set_name + str(cont) + "(self):\n\t\t"
        content += "retorno = self." + MUT.name + "("

        for x in range(0, len(MUT.params)):
            if (x == 0):
                content += self.generate_param_value(MUT, x, testset_position)
            else:
                content += ", " + self.generate_param_value(MUT, x, testset_position)
        content += ")\n\t\tself.assertTrue("
        content += self.generate_expected_output(MUT, testset_position)
        content += ")\n"
        return content
