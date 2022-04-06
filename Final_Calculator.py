import Standard_entropy_calculator
import Standard_enthalpy_formation
import Temperature_calculator
import Delta_S_surroundings
import Delta_G_calculator

class color:
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[94m'
    BLUE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
        

print(color.BOLD + 'What type of question do you want to solve?' + color.END)
print(color.RED + '1. Gibbs Free Energy (Delta G) using Delta H, Delta S and Temp' + color.END)
print(color.GREEN + '2. Gibbs Free Energy (Delta G) using Delta Suniverse and Temp' + color.END)
print(color.CYAN + '3. Standard Entropy of Reaction ΔS rxn' + color.END)
print(color.ORANGE + '4. Standard Enthalpy of Formation ΔH rxn' + color.END)
print(color.BLUE + '5. Find (Delta G) from -RT ln K' + color.END)
print(color.YELLOW + '6. Find S Universe \n' + color.END)
question_type = int(input())


if question_type == 1:
    Delta_G_calculator.delta_g_calculator_using_sys()

if question_type == 2:
    Delta_G_calculator.delta_g_calculator_using_uni()

if question_type == 3:
    Standard_entropy_calculator.standard_entropy_calculator()

if question_type == 4:
    Standard_enthalpy_formation.standard_enthalpy_formation()
    
if question_type == 5:
    print()

if question_type == 6:
    Standard_entropy_calculator.standard_entropy_calculator()
    Standard_enthalpy_formation.standard_enthalpy_formation()
    Temperature_calculator.temperature_calculator()
    Delta_S_surroundings.ssurroundings()
    Delta_S_surroundings.suniverse()
