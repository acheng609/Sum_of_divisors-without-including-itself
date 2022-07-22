#Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.

def sum_of_divisors(n):
    sum = 0
    count = 1
    
    while count < n:
        if n % count == 0:
            sum = sum + count
            count += 1
        else:
            count += 1
    return sum

print(sum_of_divisors(36))

