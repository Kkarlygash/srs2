def prime_generator():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

num_primes = int(input("Жай сан: "))

prime_gen = prime_generator()
for _ in range(num_primes):
    print(next(prime_gen))
