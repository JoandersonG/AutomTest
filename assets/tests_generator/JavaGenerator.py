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
            bottom="\n}"
        )

    def get_date_format(self, year, month, day):
        return f"new Date({int(year)}, {int(month)}, {int(day)})"

    def generate_date_output(self, v1, v2, v3):
        print(0)
        if (v1 != '' and v2 != ''):
            ymd1 = self.get_YearMonthDay_from_Date(v1)
            ymd2 = self.get_YearMonthDay_from_Date(v2)
            start_date = self.get_date_format(ymd1[0], ymd1[1], ymd1[2])
            end_date = self.get_date_format(ymd2[0], ymd2[1], ymd2[2])
            content = '(!retorno.before(' + start_date + ") " + self.and_operator + " !retorno.after(" + end_date + "))"
        if (v3 != ''):
            vals = v3.replace(" ", "").split(';')
            for x in range(0, len(vals)):
                ymd3 = self.get_YearMonthDay_from_Date(vals[x])
                date = self.get_date_format(ymd3[0], ymd3[1], ymd3[2])
                if (content != ''):
                    content += self.or_operator + 'retorno.equals(' + date + ")"
                else:
                    content += 'retorno.equals(' + date + ")"
        return content

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










