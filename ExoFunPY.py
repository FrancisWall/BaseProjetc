# -*-coding:Utf-8 -*

# Comprendre les fonctions et la différence entre print et return
# def function_that_prints():
#     print ("I printed")
#
# def function_that_returns():
#     return "I returned"
#
# f1 = function_that_prints()
# f2 = function_that_returns()
# print ("Now let us see what the values of f1 and f2 are")
# print (f1)
# print (f2)

# Exo PY elementary exo 1

# def mult_two():
#      A = int(input("Entrez le 1er nombre"))
#      B = int(input("Entrez le 2ième nombre"))
#      return A * B
# print(mult_two())

def mult_two(a: int, b: int) -> int:
    return a*b

print(mult_two(2, 3))