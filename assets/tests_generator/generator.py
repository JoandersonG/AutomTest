import datetime
import random
import re
import string


class Generator:

    def __init__(self, not_operator, and_operator, or_operator, false_syntax, true_syntax, title, bottom) -> None:
        self.not_operator = not_operator
        self.and_operator = and_operator
        self.or_operator = or_operator
        self.false_syntax = false_syntax
        self.true_syntax = true_syntax
        self.title = title
        self.bottom = bottom

    def get_YearMonthDay_from_Date(self,date):
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        splitter = '/' if date.find('/') > 0 else '-'
        if re.match(pattern, date) is not None:
            ymd = date.split(splitter)
        else:
            ymd = date.split(splitter)[::-1]

        return ymd



    def generate_Date(self, v1, v2, v3):
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
            
            return self.get_date_format(year, month, day)

        else:
            print("Data não foi preenchida corretamente.")
            return False

    def generate_String(self, value, qtd):
        signs_without_quotes = string.punctuation[0:1] + string.punctuation[2:]  # remove simbolo: "
        signs_without_quotes = signs_without_quotes[0:5] + signs_without_quotes[6:]  # remove simbolo: '

        if (qtd.find('~') == -1):
            num = int(qtd)
        else:
            vals = qtd.replace(" ", "").split('~')
            num = random.randint(int(vals[0]), int(vals[1]))

        if len(value) > 1:
            values = value.replace(" ", "").split(',')
            value = values[random.randint(1, len(values)) - 1]

        if value.casefold() == "signs" or value.casefold() == "sign":
            return ''.join([random.choice(signs_without_quotes) for n in range(num)])

        elif value.casefold() == "alphanumerics" \
                or value.casefold() == "alphanumeric" \
                or value.casefold() == "numbers/letters":
            return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(num)])

        elif value.casefold() == "any" \
                or value.casefold() == "all" \
                or value.casefold() == "any character" \
                or value.casefold() == "any_character" \
                or value.casefold() == "anycharacter":
            return ''.join([random.choice(string.ascii_letters + string.digits + signs_without_quotes) for n in range(num)])

        elif value.casefold() == "numbers" or value.casefold() == "number":
            return ''.join([random.choice(string.digits) for n in range(num)])

        elif value.casefold() == "letters" or value.casefold() == "letter":
            return ''.join([random.choice(string.ascii_letters) for n in range(num)])
        else:
            return value * num


    def generate_int(self, v1, v2, v3):
        if (v1 != '' and v2 != '' and v3 != ''):
            a = random.randint(int(v1), int(v2))
            vals = v3.replace(" ", "").split(';')
            b = random.randint(0, len(vals))
            if (b == 0):
                return str(a)
            else:
                return str(vals[b - 1])

        elif (v1 != '' and v2 != ''):
            return str(int(random.uniform(int(v1), int(v2))))

        else:
            vals = v3.replace(" ", "").split(';')
            return str(int(random.uniform(0, len(vals) - 1)))


    def generate_decimal_numbers(self, type_name, v1, v2, v3):
        if (v1 != '' and v2 != '' and v3 != ''):
            a = random.uniform(float(v1), float(v2))
            vals = v3.replace(" ", "").split(';')
            b = random.randint(0, len(vals))
            if (b == 0):
                if (type_name == 'double'):
                    return str(round(a, 6))
                else:
                    return str(round(a, 3))

            else:
                if (type_name == 'double'):
                    return str(round(float(vals[b - 1]), 6))
                else:
                    return vals[random.randint(0, len(vals) - 1)]

        elif (v1 != '' and v2 != ''):
            if (type_name == 'double'):
                return str(round(random.uniform(float(v1), float(v2)), 6))
            else:
                return str(round(random.uniform(float(v1), float(v2)), 3))

        else:
            vals = v3.replace(" ", "").split(';')
            return vals[random.randint(0, len(vals) - 1)]
    

    def generate_param_value(self, MUT, i, j):  # i = parameter order / j = testset order
        if (MUT.params[i].type_name == 'String'):
            vals1 = MUT.testsets[j].ranges[i].v1[1:len(MUT.testsets[j].ranges[i].v1) - 1].replace(" ", "").split('][')
            vals2 = MUT.testsets[j].ranges[i].v2[1:len(MUT.testsets[j].ranges[i].v2) - 1].replace(" ", "").split('][')

            content = ''
            for x in range(0, len(vals1)):
                content += self.generate_String(vals1[x], vals2[x])
            return '\"' + content + '\"'

        elif (MUT.params[i].type_name == 'char'):
            vals = MUT.testsets[j].ranges[i].v1.replace(" ", "").split(';')
            opcoes = ''
            for x in range(0, len(vals)):
                opcoes += self.generate_String(vals[x], '1')
            return "\'" + opcoes[random.randint(0, len(opcoes) - 1)] + "\'"

        elif (MUT.params[i].type_name == 'int'):
            return self.generate_int(MUT.testsets[j].ranges[i].v1, MUT.testsets[j].ranges[i].v2, MUT.testsets[j].ranges[i].v3)

        elif MUT.params[i].type_name == 'double' or MUT.params[i].type_name == 'float':
            return self.generate_decimal_numbers(MUT.params[i].type_name,
                                            MUT.testsets[j].ranges[i].v1,
                                            MUT.testsets[j].ranges[i].v2,
                                            MUT.testsets[j].ranges[i].v3)

        elif MUT.params[i].type_name == 'Date':
            return self.generate_Date(MUT.testsets[j].ranges[i].v1, MUT.testsets[j].ranges[i].v2, MUT.testsets[j].ranges[i].v3)

        else:  # boolean
            if (MUT.testsets[j].ranges[i].v1.casefold() == "true"):
                return self.true_syntax
            else:
                return self.false_syntax


    def generate_expected_output(self, MUT, i):  # i = testset order

        v1 = MUT.testsets[i].expected_range.v1
        v2 = MUT.testsets[i].expected_range.v2
        v3 = MUT.testsets[i].expected_range.v3
        content = ''
        if (MUT.output_type == 'String'):
            vals1 = v1[1:len(v1) - 1].replace(" ", "").split('][')
            vals2 = v2[1:len(v2) - 1].replace(" ", "").split('][')

            for x in range(0, len(vals1)):
                content += self.generate_String(vals1[x], vals2[x])
            content = 'retorno == \"' + content + '\"'

        elif (MUT.output_type == 'char'):
            vals = v1.replace(" ", "").split(';')
            opcoes = ''
            for x in range(0, len(vals)):
                opcoes += self.generate_String(vals[x], '1')
            provided_chars = v1.replace(" ", "").split(';')
            for character in provided_chars:
                if content != '':
                    content += self.or_operator + ' retorno == ' + character + '\''
                else:
                    content += 'retorno == \'' + character + '\' '

        elif (MUT.output_type == 'boolean'):

            if (v1.casefold() == "true"):
                content += "retorno"
            else:
                return self.not_operator + " retorno"
        elif (MUT.output_type == 'Date'):
            return self.generate_date_output(v1,v2,v3)

        else:  # if (MUT.output_type == 'int' or MUT.output_type == 'double' or MUT.output_type == 'float'):
            if (v1 != '' and v2 != ''):
                content = '(retorno >= ' + v1 + " "+ self.and_operator + ' retorno <= ' + v2 + ') '
            if (v3 != ''):
                vals = v3.replace(" ", "").split(';')
                for x in range(0, len(vals)):
                    if (content != ''):
                        content += self.or_operator + ' retorno == ' + vals[x]
                    else:
                        content += 'retorno == ' + vals[x]

        return content
    
    
    def generate_tests(self, MUT, file_path=''):
        file_location = file_path + ('' if file_path.endswith('/') else '/') + MUT.class_name + self.title
        testfile = open(file_location, 'a+')
        testfile.seek(0)
        previous = testfile.readlines()

        if len(previous) == 0:
            testfile.write(self.header_content(MUT))
        else:
            testfile.seek(0)
            testfile.truncate()
            testfile.write(''.join([a for a in previous[:-2]]))

        cont = 1
        for i in range(0, len(MUT.testsets)):
            for j in range(0, MUT.testsets[i].number_of_cases):
                testfile.write(self.test_content(MUT, MUT.testsets[i].name, cont, i))
                cont += 1

        testfile.write(self.bottom)
        testfile.close()