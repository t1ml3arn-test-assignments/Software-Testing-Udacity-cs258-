# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

import random

def get_luhn_digit(d):
    d *= 2
    if d > 9:
        return d - 9
    else:
        return d

def get_luhn_checksumm(n: int):
   
    num = str(n)
    # the last digit is going directly to the checksum
    checksum = int(num[-1:])
    
    # number with EVEN number of digits
    if len(num) % 2 == 0:
        # note `-1` - we don't need to check the LAST digit
        for i in range(0, len(num)-1, 2):
            odd_digit = int(num[i])
            checksum += get_luhn_digit(odd_digit)

        for i in range(1, len(num)-1, 2):
            checksum += int(num[i])
    else:
    # number with ODD number of digits
        # again, note `-1` - we don't need to work with the last digit 
        for i in range(1, len(num)-1, 2):
            even_digit = int(num[i])
            checksum += get_luhn_digit(even_digit)
        
        for i in range(0, len(num)-1, 2):
            checksum += int(num[i])

    return checksum % 10

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
def is_luhn_valid(n: int):

    return get_luhn_checksumm(n) == 0

print(is_luhn_valid(1234))
print(is_luhn_valid(4408041234567890)) # should be not valid
print(is_luhn_valid(4408041234567893)) # should be valid
print(is_luhn_valid(4417123456789112)) # should be not valid
print(is_luhn_valid(4417123456789113)) # should be valid

# so now lets generate random VALID credit card numbers
def generate(prefix: int, n: int):
    # 1. find how many nums we need to fill up to limit n
    # 2. get random data and build credit card num
    # 3. correct that num
    # 4. return
    card_num = str(prefix)
    num_digits_to_get = n - len(card_num)
    assert num_digits_to_get > 0

    for i in range(0, num_digits_to_get):
        card_num += str(random.randint(0, 9))
    
    checksumm = get_luhn_checksumm(card_num)
    check_digit = int(card_num[-1:])
    # correect the num if it is invalid
    if checksumm != 0:
        check_digit += (10 - checksumm)
        check_digit %= 10
        card_num = card_num[:-1] + str(check_digit)

    # if assertion is raised - something really bad happened
    assert is_luhn_valid(card_num)

    return card_num
