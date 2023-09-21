# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except:
#     print("We have an error")
# print("code after capsule")

# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)

# try:
#     try:
#         print("start code")
#         print(error)
#         print("No errors")
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)

# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can’t workwith {type(var_1)}, "
#                         f"we need class str")
#     else:
#         return var_1
# first_var = "Hello"
# checker(first_var)

# class BuildingEror(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return print("enough material")
#     else:
#         raise BuildingEror(amount_of_material)
# materials = 123
# check_material(materials, 300)

import warnings
warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("always", ImportWarning)
warnings.warn("Warning, no code here", SyntaxWarning)
warnings.warn("Warning, module not imporrt", ImportWarning)