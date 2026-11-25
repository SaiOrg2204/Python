from test_fun import num_days

days = 10
def call_days(days):
    print(days > 0)
    if days > 0:
        print(days)
        return f"Number of hours are {days * 24}"
    elif days == 0:
        return f"Number of days are zero"
    else:
        return f"Given number is invalid"
def input_validate(num_days):
    if num_days.isdigit():
        print("data type of given input is", type(num_days))
        num_days = int(num_days)
        print("data type after converting is", type(num_days))
        # ret_value = call_days(num_days)
        # print(ret_value)
        print(call_days(num_days))  # calling function without any additional variable and print return value
    else:
        print("Invalid data type has given, please enter a valid input type")

num_days = input("enter number of days \n")
input_validate(num_days)




