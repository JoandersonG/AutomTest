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
        
    def get_date_format(self, year, month, day):
        return f"new Date(\"{year}-{month}-{day}\")"

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
                date = self.get_date_format(ymd3[0], ymd3[1], ymd3[2])
                if (content != ''):
                    content += self.or_operator + ' retorno.getTime() === ' + date + ".getTime()"
                else:
                    content += 'retorno.getTime() === ' + date + ".getTime()"
        return content

    def header_content(self, MUT):
        content = ''
        # if (MUT.package_name != ''):
        #     content += "package " + MUT.package_name + ";\n"
        content += "describe( \""
        content += MUT.class_name + " Tests \", () => {\n\tlet objeto;\n"
        content += "\n\tbeforeEach(() => {\n\t\tobjeto = new " + MUT.class_name + "(coloque os parametros)\n\t});\n"
        return content


    def test_content(self, MUT, test_set_name, cont, testset_position):
        content = "\n\tit(\"test " + test_set_name + str(cont) + "\", () => {\n\t\t"
        content +="const retorno = objeto." + MUT.name + "("

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



