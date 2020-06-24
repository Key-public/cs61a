####
# 1) we'll start off with something familiar. without looking at sum digits, 
#    implement the following function so that md(number) returns the PRODUCT of the 
#    digits of number.
#    
#    md(4023) -> 4 * 0 * 2 * 3 = 0
#    md(423) -> 4 * 2 * 3 = 24
####

def md(number):
    if number < 10:
        return number

    current_digit = number % 10
    floor_divided_by_10 = number // 10

    return current_digit * md(floor_divided_by_10)

print(md(4023))
print(md(423))

####
# 2) Exponents are basically repeated multiplication! For example,
#    2^3 (2 to the power of 3) = 2 * 2 * 2 = 8
#    Basically, it's three 2's multiplied together.
#    We can write a function for this recursively! 
#    2 is the base, and 3 is the exponent in this case.
#    So, for base ^ exponent, write the following function that returns that value!
#    
#    HINT: remember when we did factorial, we thought about how we have to 
#    make the problem smaller, and tried to relate the smaller problem
#    to our original problem. That may help here!
#
#    rec_power(2, 3) = 2 * 2 * 2 = 8
#    rec_power(4, 2) = 4 * 4 = 16
#
####

def rec_power(base, exponent):
    if exponent <= 0:
        return 1

    exponent = exponent - 1

    return base * rec_power(base, exponent)

print(rec_power(2, 3))
print(rec_power(4, 2))

####
# 3) Implement the following function so that count8(number)
#    counts the number of times the number "8" appears in number.
#    
#    I've given you parts of the base cases; if the number left is 8, we've
#    found an 8, so what should we return?
#    If the number left isn't 8, but can't be made any smaller, what should
#    we return then?
#
#    count8(3283) -> 1
#    count8(32883) -> 2
#    count8(8388) -> 3
####

def count8(number):
    if number == 8:
        return 1
    elif number < 10:
        return 0

    rightmost_digit = number % 10
    rest_of_number = number // 10

    if rightmost_digit == 8:
        return 1 + count8(rest_of_number)
    else:
        return count8(rest_of_number)

print(count8(3283))
print(count8(32883))
print(count8(8388))