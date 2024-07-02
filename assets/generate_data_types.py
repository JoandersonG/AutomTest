import datetime
import random
import re
import string

def get_YearMonthDay_from_Date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    splitter = '/' if date.find('/') > 0 else '-'
    if re.match(pattern, date) is not None:
        ymd = date.split(splitter)
    else:
        ymd = date.split(splitter)[::-1]

    return ymd


def generate_Date(v1, v2, v3):
    print('generate_Date v1=' + v1 + ' v2=' + v2)
    if v1 != '' and v2 != '':

        ymd1 = get_YearMonthDay_from_Date(v1)
        ymd2 = get_YearMonthDay_from_Date(v2)

        start_date = datetime.date(int(ymd1[0]), int(ymd1[1]), int(ymd1[2]))
        end_date = datetime.date(int(ymd2[0]), int(ymd2[1]), int(ymd2[2]))

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        return str(random_date)

    else:
        print("Data não foi preenchida corretamente.")
        return False


def generate_String(value, qtd):
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


def generate_int(v1, v2, v3):
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


def generate_decimal_numbers(type_name, v1, v2, v3):
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
    