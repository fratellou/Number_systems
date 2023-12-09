def convert_number(number, from_base, to_base):
    if from_base not in [2, 8, 16, 10] or to_base not in [2, 8, 16, 10]:
        return "NULL"
    if number[0] == '-':
        return "NULL"

    # Converting a number to decimal notation
    if "." in number:
        integer_part, decimal_part = number.split(".")

        # Converting the integer part
        integer_part = int(integer_part, from_base)
        if (to_base == 10): result_integer = str(integer_part)
        elif (to_base == 2): result_integer = bin(integer_part)[2:]
        elif (to_base == 8): result_integer = oct(integer_part)[2:]
        elif (to_base == 16): result_integer = hex(integer_part)[2:]

        # Converting the decimal part
        precision = 2
        decimal_part = int(decimal_part, from_base)
        result_decimal = ""

        for _ in range(precision):
            if decimal_part == 0:
                break

            quotient = decimal_part * to_base // from_base
            remainder = decimal_part * to_base % from_base

            result_decimal += str(quotient)
            decimal_part = remainder

        if to_base == 10: return result_integer + '.' + result_decimal
        elif to_base == 2: return result_integer + '.' + bin(int(result_decimal))[2:]
        elif to_base == 8: return result_integer + '.' + oct(int(result_decimal))[2:]
        elif to_base == 16: return result_integer + '.' + hex(int(result_decimal))[2:]

    else:
        number = int(number, from_base)
        if (to_base == 10): return str(number)
        elif (to_base == 2): return bin(number)[2:]
        elif (to_base == 8): return oct(number)[2:]
        elif (to_base == 16): return hex(number)[2:]
