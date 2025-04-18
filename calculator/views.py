from django.shortcuts import render
import operator

def calculator_view(request):
    result = None
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    operation = request.POST.get("operation")

    if num1 and num2 and operation:
        try:
            num1, num2 = float(num1), float(num2)
            operations = {
                "add": operator.add,
                "subtract": operator.sub,
                "multiply": operator.mul,
                "divide": operator.truediv,
                "modulus": operator.mod,
                "power": operator.pow,
            }

            if operation in operations:
                result = operations[operation](num1, num2)
            else:
                result = "Invalid Operation"

        except ValueError:
            result = "Invalid Input"
        except ZeroDivisionError:
            result = "Cannot divide by zero"

    return render(request, "calculator.html", {"result": result})
