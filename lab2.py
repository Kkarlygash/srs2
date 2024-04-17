def quat_gen(exponent):

    def quat_func(x):
        return x ** exponent

    return quat_func

kvadrat = quat_gen(2)

kub = quat_gen(3)

number = 5
kvadrat_result = kvadrat(number)
kub_result = kub(number)

print(f"{number} квадраты: {kvadrat_result}")
print(f"{number} кубы: {kub_result}")
