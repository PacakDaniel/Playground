def fibonacci(num1: int, num2: int, limit: int) -> list:
    """
    return a fibonacci list with the starting numbers num1 and num2 below the limit

    :param num1: first entry of the fibonacci list
    :param num2: second entry of the fibonacci list
    :param limit: max value of the list
    :return: list if integers representing a fibonaci list
    """
    smallNum = min(num1, num2)
    bigNum = max(num1, num2)

    fibonacci = []
    fibonacci.append(num1)
    fibonacci.append(num2)
    while (True):
        nextNum=smallNum + bigNum
        smallNum = bigNum
        bigNum = nextNum
        if nextNum <= limit:
            fibonacci.append(nextNum)
        else :
            return fibonacci

print('asd')