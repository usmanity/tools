import re
import sys

number = int(sys.argv[1])

def is_prime (num):
    return re.match(r"^1?$|^(11+?)\1+$",'1'*num) is None

if (is_prime(number)):
    print("%d is a prime number" % (number))
else:
    print("%d is not a prime number" % (number))
