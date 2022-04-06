# Below is the Temperature Calculator
def temperature_calculator(): 
    global temp_value
    temp_value = float(input('What is the temp? '))
    temp_type = input('Is it in (K/C)? ')
    temp_type = temp_type.lower()

    if temp_type == "k":
        temp_value = temp_value
    elif temp_type == "c":
        temp_value = temp_value + 273.15
    else:
        print('Error unsupported value type. ')

    print(temp_value)


