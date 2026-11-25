days = 10  # Global variable, this can be accesable throughout the program
def cal_days(days):
    return days * 24 * 60 # 'days' is a local variable, scope of the var is with in this function only.
    expr = days * 24 * 60
    print("This is a function definition and number of days are", days)
    print(f"number of minutes are {expr}")
    print("number of minutes are", expr, days)
    #return expr
print("This is a function call")
cal_days(15) # function call
cal_days(20)
cal_days(30)
num_days=input("Enter the number of days \n") # Taking user inputs
print("number of days given by user is", num_days)
num_days = int(num_days)
print(cal_days(num_days))   # by default input function consider the inputs as strings.
                          # we need to convert them as int when we passing them to functions.



