def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("n санын енгізіңіз: "))
if n < 0:
    print("оң санын енгізіңіз")
else:
    result = fibonacci(n)
    print("Фиббоначи:", result)
