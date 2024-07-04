from generate_data_types import generate_Date, generate_String, generate_int, generate_decimal_numbers
import random

#TODO falta resolver a importação e o Date

def generate_expected_output_python(MUT, i):  #Falta testar o date

    v1 = MUT.testsets[i].expected_range.v1
    v2 = MUT.testsets[i].expected_range.v2
    v3 = MUT.testsets[i].expected_range.v3
    content = ''
    if (MUT.output_type == 'String'):
        vals1 = v1[1:len(v1) - 1].replace(" ", "").split('][')
        vals2 = v2[1:len(v2) - 1].replace(" ", "").split('][')

        for x in range(0, len(vals1)):
            content += generate_String(vals1[x], vals2[x])
        content = 'retorno == \"' + content + '\"'

    elif (MUT.output_type == 'char'):
        vals = v1.replace(" ", "").split(';')
        opcoes = ''
        for x in range(0, len(vals)):
            opcoes += generate_String(vals[x], '1')
        provided_chars = v1.replace(" ", "").split(';')
        for character in provided_chars:
            if content != '':
                content += ' or retorno == \'' + character + '\''
            else:
                content += 'retorno == \'' + character + '\''

    elif (MUT.output_type == 'boolean'):

        if (v1.casefold() == "true"):
            content += "retorno"
        else:
            return "not retorno"

    else:  # if (MUT.output_type == 'int' or MUT.output_type == 'double' or MUT.output_type == 'float'):
        if (v1 != '' and v2 != ''):
            content = '(retorno >= ' + v1 + ' and retorno <= ' + v2 + ')'
        if (v3 != ''):
            vals = v3.replace(" ", "").split(';')
            for x in range(0, len(vals)):
                if (content != ''):
                    content += ' or retorno == ' + vals[x]
                else:
                    content += 'retorno == ' + vals[x]

    return content


def generate_param_value_python(MUT, i, j):  #Falta testar o date
    if (MUT.params[i].type_name == 'String'):
        vals1 = MUT.testsets[j].ranges[i].v1[1:len(MUT.testsets[j].ranges[i].v1) - 1].replace(" ", "").split('][')
        vals2 = MUT.testsets[j].ranges[i].v2[1:len(MUT.testsets[j].ranges[i].v2) - 1].replace(" ", "").split('][')

        content = ''
        for x in range(0, len(vals1)):
            content += generate_String(vals1[x], vals2[x])
        return '\"' + content + '\"'

    elif (MUT.params[i].type_name == 'char'):
        vals = MUT.testsets[j].ranges[i].v1.replace(" ", "").split(';')
        opcoes = ''
        for x in range(0, len(vals)):
            opcoes += generate_String(vals[x], '1')
        return "\'" + opcoes[random.randint(0, len(opcoes) - 1)] + "\'"

    elif (MUT.params[i].type_name == 'int'):
        return generate_int(MUT.testsets[j].ranges[i].v1, MUT.testsets[j].ranges[i].v2, MUT.testsets[j].ranges[i].v3)

    elif MUT.params[i].type_name == 'double' or MUT.params[i].type_name == 'float':
        return generate_decimal_numbers(MUT.params[i].type_name,
                                        MUT.testsets[j].ranges[i].v1,
                                        MUT.testsets[j].ranges[i].v2,
                                        MUT.testsets[j].ranges[i].v3)

    elif MUT.params[i].type_name == 'Date':#TODO
        return generate_Date(MUT.testsets[j].ranges[i].v1, MUT.testsets[j].ranges[i].v2, MUT.testsets[j].ranges[i].v3)

    else:  # boolean
        if (MUT.testsets[j].ranges[i].v1.casefold() == "true"):
            return "True"
        else:
            return "False"


def test_content_python(MUT, test_set_name, cont, testset_position): #DONE
    content = "\n\tdef test_" + test_set_name + str(cont) + "(self):\n\t\t"
    content += "retorno = self." + MUT.name + "("

    # TO DO: gerar valores
    for x in range(0, len(MUT.params)):
        if (x == 0):
            content += generate_param_value_python(MUT, x, testset_position)
        else:
            content += ", " + generate_param_value_python(MUT, x, testset_position)

    content += ")\n\t\tself.assertTrue("
    content += generate_expected_output_python(MUT, testset_position)
    content += ")\n"
    return content


def header_content_python(MUT): #Falta importar a classe
    content = ''
    if (MUT.package_name != ''):
        content += "package " + MUT.package_name + ";\n"
    content += "import unittest\n\nclass "
    content += MUT.class_name + "Test(unittest.TestCase," + MUT.class_name + "):\n"
    return content


def generate_tests_python(MUT, file_path=''):#DONE
    file_location = file_path + ('' if file_path.endswith('/') else '/') + MUT.class_name + 'Test.py'
    testfile = open(file_location, 'a+')
    testfile.seek(0)
    previous = testfile.readlines()

    if len(previous) == 0:
        testfile.write(header_content_python(MUT))
    else:
        testfile.seek(0)
        testfile.truncate()
        testfile.write(''.join([a for a in previous[:-2]]))

    cont = 1
    for i in range(0, len(MUT.testsets)):
        for j in range(0, MUT.testsets[i].number_of_cases):
            testfile.write(test_content_python(MUT, MUT.testsets[i].name, cont, i))
            cont += 1
    testfile.write('\nif __name__ == "__main__":\n\tunittest.main()')
    testfile.close()
