"""List of prime numbers generator."""

def primes(number_of_primes):
    list = [2]
    j = 2
    while (len(list) < number_of_primes):
        for prime in list:
            if j%prime==0:
                break
        else:
            list.append(j)
            j += 1
    return list
