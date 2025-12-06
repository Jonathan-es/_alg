# 111210554

def calc_pow_exp(x):
    return pow(2, x)

def calc_pow_loop(x):
    value = 1
    count = x
    while count > 0:
        value = value * 2
        count -= 1
    return value

def calc_pow_rec(x):
    if x == 0:
        return 1
    if x & 1 == 0:
        temp = calc_pow_rec(x // 2)
        return temp * temp
    return 2 * calc_pow_rec(x - 1)

def calc_pow_bit(x):
    base = 1
    base <<= x
    return base


if __name__ == "__main__":
    num = 10

    print("exp:", calc_pow_exp(num))
    print("loop:", calc_pow_loop(num))
    print("rec :", calc_pow_rec(num))
    print("bit :", calc_pow_bit(num))
