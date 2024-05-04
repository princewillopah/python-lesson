# try:
#     a = int(input("enter num1: "))
#     b = int(input("enter num2: "))
#     print("{}+{}={}".format(a,b,a+b))
# except TypeError:
#         print("TYPE ERROR FOUND ")
#         # print(str(a)+"+"+str(b)+" = ERROR")
# finally:
#     print("\nTHE END!")
# ------------------------------------
# while True:
#   try:
#     a = int(input("enter num1: "))
#     break
#   except:
#       print("invalid imput")



# # define python user-defined exception
# class Error(Exception):
#     """base class for the exception"""
#     pass
# class ValueTooSmallError(Error):
#     """Raised when the value of the imput is too small"""
#
# class ValueTooLargeError(Error):
#     """Raised when the value of the imput is too small"""
#
# number = 10
# while True:
#     try:
#       i_num = int(input("Enter number: "))
#       if i_num < number:
#          raise ValueTooSmallError
#       elif i_num > number:
#         raise ValueTooLargeError
#       break
#     except ValueTooSmallError:
#         print("the value is too small, try again")
#         print()
#     except ValueTooLargeError:
#         print("the value is too LARGE, try again")
#         print()
# print("Congratulation! you guessed it correctly")