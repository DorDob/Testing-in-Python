# też się da wykonać funkcję factorial w ten sposób:
# # import math
#
# print(math.factorial(4))

def factorial(n):
    if type(n) != int:  # na samej górze, jeżeli to nie jest int, to nie robi testu
        return False
    if n > 0:  # pass
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result
    elif n == 0:
        return 1
    else:
        return False


if __name__ == "__main__":  # dzięki temu kod poniżej nie zostanie zaimportowany do testów i się w nich nie wykona
    print(factorial(-1))
    print(factorial(0))
    print(factorial(1))




