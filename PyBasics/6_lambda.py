# Lambda function is alternative to a traditional function (similar to arrow function in js)


def give_1():
    return 1


give_1_lambda = lambda: 1

result = give_1()
result = give_1_lambda()
