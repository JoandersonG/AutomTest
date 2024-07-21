from Generator import Generator
import random
import datetime

class JavascriptGenerator(Generator):


    def __init__(self):
        super().__init__( 
                 or_operator='||', 
                 and_operator='&&', 
                 not_operator='!', 
                 true_syntax='true', 
                 false_syntax='false', 
                 title='.spec.js', 
                 bottom="\n})"
                 )
        

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
            print(random_date)
            print(type(random_date))
            
            return f"new Date(\"{random_date}\")"

        else:
            print("Data não foi preenchida corretamente.")
            return False

    def header_content(self, MUT):
        content = ''
        # if (MUT.package_name != ''):
        #     content += "package " + MUT.package_name + ";\n"
        content += "describe( \""
        content += MUT.class_name + " Tests \", () => {\n"
        return content


    def test_content(self, MUT, test_set_name, cont, testset_position):
        content = "\n\tit(\" test " + test_set_name + str(cont) + "\", () => {\n\t\t"
        content +="const retorno = " + MUT.name + "("

        # TO DO: gerar valores
        for x in range(0, len(MUT.params)):
            if (x == 0):
                content += self.generate_param_value(MUT, x, testset_position)
            else:
                content += ", " + self.generate_param_value(MUT, x, testset_position)

        content += ")\n\t\texpect("
        content += self.generate_expected_output(MUT, testset_position)
        content += ").toBeTruthy()\n\t})\n"
        return content



