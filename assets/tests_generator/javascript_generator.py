from generate_data_types import generate_Date, generate_String, generate_int, generate_decimal_numbers
import random

#TODO falta resolver a importação , o output quano é um numero e o Date

def generate_param_value_javascript(MUT, i, j):  # i = parameter order / j = testset order
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

    elif MUT.params[i].type_name == 'Date':
        return generate_Date(MUT.testsets[j].ranges[i].v1, MUT.testsets[j].ranges[i].v2, MUT.testsets[j].ranges[i].v3)

    else:  # boolean
        if (MUT.testsets[j].ranges[i].v1.casefold() == "true"):
            return "true"
        else:
            return "false"


def header_content_javascript(MUT):
    content = ''
    if (MUT.package_name != ''):
        content += "package " + MUT.package_name + ";\n"
    content += "import org.junit.*;\nimport static org.junit.Assert.assertTrue;\n\ndescribe( \""
    content += MUT.class_name + " Tests \", () => {\n"
    return content


def generate_expected_output_javascript(MUT, i):  # i = testset order

    v1 = MUT.testsets[i].expected_range.v1
    v2 = MUT.testsets[i].expected_range.v2
    v3 = MUT.testsets[i].expected_range.v3
    content = ''
    if (MUT.output_type == 'String'):
        vals1 = v1[1:len(v1) - 1].replace(" ", "").split('][')
        vals2 = v2[1:len(v2) - 1].replace(" ", "").split('][')

        for x in range(0, len(vals1)):
            content += generate_String(vals1[x], vals2[x])

    elif (MUT.output_type == 'char'):
        vals = v1.replace(" ", "").split(';')
        opcoes = ''
        for x in range(0, len(vals)):
            opcoes += generate_String(vals[x], '1')
        provided_chars = v1.replace(" ", "").split(';')
        for character in provided_chars:
            if content != '':
                content += ' ||\'' + character + '\''
            else:
                content += character

    elif (MUT.output_type == 'boolean'):

        if (v1.casefold() == "true"):
            content += "true"
        else:
            return "false"

    else:  # if (MUT.output_type == 'int' or MUT.output_type == 'double' or MUT.output_type == 'float'): #TODO
        if (v1 != '' and v2 != ''):
            content = '(retorno >= ' + v1 + ' && retorno <= ' + v2 + ')'
        if (v3 != ''):
            vals = v3.replace(" ", "").split(';')
            for x in range(0, len(vals)):
                if (content != ''):
                    content += ' || retorno == ' + vals[x]
                else:
                    content += 'retorno == ' + vals[x]

    return content


def test_content_javascript(MUT, test_set_name, cont, testset_position):
    content = "\n\tit(\" test " + test_set_name + str(cont) + "\", () => {\n\t\t"
    content +="const retorno = " + MUT.name + "("

    # TO DO: gerar valores
    for x in range(0, len(MUT.params)):
        if (x == 0):
            content += generate_param_value_javascript(MUT, x, testset_position)
        else:
            content += ", " + generate_param_value_javascript(MUT, x, testset_position)

    content += ")\n\t\texpect(retorno).toEqual("
    content += generate_expected_output_javascript(MUT, testset_position)
    content += ")\n\t})\n"
    return content


def generate_tests_javascript(MUT, file_path=''):
    file_location = file_path + ('' if file_path.endswith('/') else '/') + MUT.class_name + '.spec.js'
    testfile = open(file_location, 'a+')
    testfile.seek(0)
    previous = testfile.readlines()

    if len(previous) == 0:
        testfile.write(header_content_javascript(MUT))
    else:
        testfile.seek(0)
        testfile.truncate()
        testfile.write(''.join([a for a in previous[:-1]]))

    cont = 1
    for i in range(0, len(MUT.testsets)):
        for j in range(0, MUT.testsets[i].number_of_cases):
            testfile.write(test_content_javascript(MUT, MUT.testsets[i].name, cont, i))
            cont += 1

    testfile.write("\n})")
    testfile.close()

