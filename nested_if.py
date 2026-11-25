def process_input(input_data):
    return f"Number of hours for {input_data} days is {input_data * 24}"

def validate_input(input_data):
    print("Given value is", input_data, "and it's dats type is", type(input_data))
    if input_data.isdigit():
        input_data = int(input_data)
        if input_data > 0:
            input_data = process_input(input_data)
            return input_data
        elif input_data == 0:
            return f"GIven value is zero, please enter value greater then 0"
    else:
        return f"Given data type is not integer\n"
input_data = input("Enter number of days to calculate \n")
print(validate_input(input_data))