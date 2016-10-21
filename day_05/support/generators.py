#####################################################
def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

#####################################################
def my_generator():
    handle = open('lulu_mix_16.csv')
    handle.next()
    for line in handle:
        title = line.split(',')[0]
        title = title.upper()
        yield title

r = my_generator()

#####################################################
def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1