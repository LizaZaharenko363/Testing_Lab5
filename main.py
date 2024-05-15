def check_params(par2, par3, par4, array1):
    if not isinstance(par2, bool):
        raise TypeError("par2 має бути типу bool")
    result = 0
    m = 0

    while m < len(array1):
        if par2:
            if array1[m] % par3 == 0:
                result += array1[m]
        else:
            if array1[m] % par4 == 0:
                result += array1[m]

        m += 1

    return result


print(check_params(True, 3, 5, [3, 5, 6, 10, 12]))
print(check_params(False, 2, 7, [1, 4, 14, 52, 2]))
print(check_params(False, 5, 1, [3, 9, 10, 11, 42]))
