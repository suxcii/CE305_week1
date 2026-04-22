def parse_number(num_str):
    digits = []
    i = 0
    while i < len(num_str):
        if num_str[i] == '-':
            j = i + 1
            while j < len(num_str) and num_str[j] != '-':
                j += 1
            digits.append(int(num_str[i+1:j]))
            i = j + 1
        else:
            digits.append(int(num_str[i]))
            i += 1
    return digits


def is_valid(digits, base):
    return all(0 <= d < base for d in digits)


def to_base10(digits, base):
    value = 0
    power = len(digits) - 1
    for d in digits:
        value += d * (base ** power)
        power -= 1
    return value


def from_base10(num, new_base):
    if num == 0:
        return "0"
    
    digits = []
    while num > 0:
        digits.append(num % new_base)
        num //= new_base
    
    digits.reverse()
    
    result = ""
    for i, d in enumerate(digits):
        if d >= 10:
            if i == 0:
                result += f"-{d}"
            else:
                result += f"-{d}"
        else:
            result += f"-{d}" if i != 0 else str(d)

    if digits[-1] >= 10:
        result += "-"

    return result

def base_conv(num_str, base, new_base):
    digits = parse_number(num_str)
    
    if not is_valid(digits, base):
        return "Invalid input: digit exceeds base"
    
    base10 = to_base10(digits, base)
    return from_base10(base10, new_base)