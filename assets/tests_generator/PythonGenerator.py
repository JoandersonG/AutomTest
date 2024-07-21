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
    
    def generate_Date(self, v1, v2, v3):
        print('generate_Date v1=' + v1 + ' v2=' + v2)
        if v1 != '' and v2 != '':

            ymd1 = self.get_YearMonthDay_from_Date(v1)
            ymd2 = self.get_YearMonthDay_from_Date(v2)

            start_date = datetime.date(int(ymd1[0]), int(ymd1[1]), int(ymd1[2]))
            end_date = datetime.date(int(ymd2[0]), int(ymd2[1]), int(ymd2[2]))

            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            day = random_date.day
            month = random_date.month
            year = random_date.year

            return f'datetime.datetime({year}, {month}, {day})'

        else:
            print("Data não foi preenchida corretamente.")
            return False
        
    def has_date_type(self,MUT):
        for i in range(0, len(MUT.params)):
            if MUT.params[i].type_name == 'Date':
                return True
        return False

    def header_content(self,MUT): #Falta importar a classe
        content = ''
        if self.has_date_type(MUT):
            content += "import datetime\n"
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
