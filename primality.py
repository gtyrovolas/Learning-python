
primes = []

def sieve():
    for i in range(2, 100):
        div = False
        for p in primes:
            if(i % p == 0):
                div = True
                break
        if(not div):
            primes.append(i)
            print(i)

sieve()

        

