#compute the expression
print(((2 ** 2 * 5) + 10 > 20 and not(False or True)) or (15<=15 and 8 != 12))

# Compute the expression
result1 = (
    (4 ** 3 - 7 * 12 + 3 < 0 or not (True and False)) and
    (5 > 8 or 4 != 7)
)
print(result1)

# Compute the expression
result2 = (
    (((3 ** 2 + 2 * 6) <= 7 or True) and not (False or (4 >= 8))) or
    (10 == 10 and 3 != 2)
)
print(result2)

# Compute the expression
result3 = (
    (2 ** 5 - 3 * 6 < 0 and (False or not True)) or
    (7 == 12 and 9 > 2)
)
print(result3)

#compute the expression
result4=((((7 ** 2 + 5 * 10) // 3 > 6 and (True or not False)) or ((8 - 12) % 7 <= 5 and (6 or not True))) and(not (False or 12) and (7 ** 2 - 2 * 5 != 10))) or((6 and not (8 < 12 and 2 > 3)) or (7 + 5 * 10 == 6 and not False))

print(result4)

print({10,20} < {10,20,30,40}) #True
#it checks whether the whole set is present in another set or not (it will not search for the each and every element bcz set is unordered)
print({10,20} < {30,40}) #False

print((10,20) == (10,20))
print([10,20]==-[10,20])