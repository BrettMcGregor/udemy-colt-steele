def calculate(message="The result is ", **kwargs):
    op_dict = {"add": "+", "subtract": "-", "divide": "/", "multiply": "*"}
    if kwargs["make_float"]:
        return message + str(eval(str(kwargs["first"]) + op_dict[kwargs["operation"]] + str(kwargs["second"])))
    if not kwargs["make_float"]:
        return message + " " + str(int(eval(str(kwargs["first"]) + op_dict[kwargs["operation"]] + str(kwargs["second"]))))


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
