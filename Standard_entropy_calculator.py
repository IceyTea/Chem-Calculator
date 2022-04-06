# THIS WHOLE SECTION TO FIND STANDARD ENTROPY vvvvvvvvvvvvvvvvvvvvvvvv
# Ssystem = Sproducts - Sreactants

def standard_entropy_calculator():
    global delta_s_final
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        
    products_value = []
    products = int(input(color.BOLD + color.PURPLE + 'How many products do you have for Delta S: \n' + color.END))
    intital = 0
    question_number = 1
    while intital < products:
        moles_p = float(input(color.RED + f'How many moles for product #{question_number}: \n' + color.END))
        delta_s_value_p = float(input(color.UNDERLINE + f'What is the S° value for product #{question_number}:\n' + color.END))
        Sproduct = moles_p * delta_s_value_p
        question_number += 1
        
        products_value.extend([Sproduct])
        intital += 1

        if intital == products:
            break

    reactants_value=[]
    intital = 0
    reactants = int(input(color.BOLD + color.PURPLE + 'How many reactants do you have for Delta S?: \n' + color.END))
    question_number = 1
    while intital < reactants:
        moles_r = float(input(color.RED + f'How many moles for reactant #{question_number}: \n' + color.END))
        delta_s_value_r = float(input(color.UNDERLINE + f'What is the S° value for reactant #{question_number}:\n' + color.END))
        Sreactant = moles_r * delta_s_value_r
        question_number += 1
        
        reactants_value.extend([Sreactant])
        intital += 1

        if intital == reactants:
            break
    delta_s_final = sum(products_value) - sum(reactants_value)
    if delta_s_final > 0:
        print(color.BOLD + f'''Your S°rxn is {delta_s_final:.3f} (J/mol*K)
        The reaction is spontaneous''')
    else:
        print(color.BOLD + f'''Your S°rxn is {delta_s_final:.3f} (J/mol*K)
        The reaction is not spontaneous''')

# THIS WHOLE SECTION TO FIND STANDARD ENTROPY ^^^^^^^^^^^^^^^^^^^^^^^^^^