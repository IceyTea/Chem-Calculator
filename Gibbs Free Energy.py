

# Ssystem = Sproducts - Sreactants
boltzmann_constant = 1.38 * (10 ** -23)
def standard_entropy_calculator():
    products = int(input('How many products do you have? '))
    intital = 0
    while intital < products:
        moles_p = int(input('How many moles for product? '))
        delta_s_value_p = float(input('What is the S° value for product? '))
        Sproduct = moles_p * delta_s_value_p
        intital += 1
        if intital == products:
            break
    intital = 0
    reactants = int(input('How many reactants do you have? '))
    while intital < reactants:
        moles_r = int(input('How many moles for reactant? '))
        delta_s_value_r = float(input('What is the S° value for reactant'))
        Sreactant = moles_r * delta_s_value_r
        intital += 1
        if intital == products:
            break

    print(Sproduct)
    print(Sreactant)



question_type = int(input('''What type of question do you want to solve?
1. Gibbs Free Energy
2. Gibbs Free Energy at Non Standard Conditions
3. Standard Entropy of Reaction ΔS°
4. Number of Microstates  '''))

if question_type == 3:
    standard_entropy_calculator()


# Entropy Units are J/K
# Entropy is Delta System = S final - S initial 
# Standard Molar Entropy = J/(Mol * K), Gases 1atm, Solution 1 molar
# When Temp increases, Entropy Increases -> Increase in kinetic energy -> more microstates = more energy
# Entropy Increases in Solid -> Liquid -> Gas
# If Delta S > 0 = Spontanious, if Delta S < 0 = Nonspontanious








        



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



