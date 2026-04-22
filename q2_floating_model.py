def floating_model(num):
    sign = 1 if num < 0 else 0
    num = abs(num)

    integer_part = int(num)
    fraction_part = num - integer_part

    int_bin = bin(integer_part)[2:]

    frac_bin = ""
    while len(frac_bin) < 10 and fraction_part != 0:
        fraction_part *= 2
        bit = int(fraction_part)
        frac_bin += str(bit)
        fraction_part -= bit

    if integer_part != 0:
        shift = len(int_bin) - 1
        mantissa = int_bin[1:] + frac_bin
    else:
        shift = 0
        while frac_bin[shift] == '0':
            shift += 1
        shift += 1
        mantissa = frac_bin[shift:]
        shift = -shift

    exponent = shift + 15
    exponent_bin = format(exponent, '05b')

    mantissa = (mantissa + "00000000")[:8]

    return f"{sign}_{exponent_bin}_{mantissa}"