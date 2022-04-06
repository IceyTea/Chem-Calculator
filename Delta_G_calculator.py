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
    

def delta_g_calculator_using_sys():
    delta_h = float(input(color.ORANGE + 'What is ΔHsys(standard)?\n' + color.END))
    delta_s = float(input(color.RED + 'What is ΔSys(standard)\n'+ color.END))
    delta_g_type = input(color.CYAN + 'Do you want ΔG in J or kJ?\n' + color.END)
    delta_g_type = delta_g_type.lower()
    if delta_g_type == "j":
        print('\n')
        delta_g_sys = (delta_h * 1000) - (298 * delta_s)
        if delta_g_sys < 0:
            print(f'''ΔG(system) is {delta_g_sys:.3f} (J/mol) 
The reaction is spontaneous since ΔG < 0''')
        elif delta_g_sys > 0:
            print(f'''ΔG(system) is {delta_g_sys:.3f} (J/mol) 
The reaction is not spontaneous since ΔG > 0''')
        elif delta_g_sys == 0:
            print(f'''ΔG(system) is {delta_g_sys:.3f} (J/mol) 
The reaction is at equlibrium since ΔG = 0''')
    elif delta_g_type == "kj":
        delta_g_sys = delta_h - (298 * (delta_s / 1000))
        if delta_g_sys < 0:
            print(f'''ΔG(system) is {delta_g_sys:.3f} (kJ/mol) 
The reaction is spontaneous since ΔG < 0''')
        elif delta_g_sys > 0:
            print(f'''ΔG(system) is {delta_g_sys:.3f} (kJ/mol) 
The reaction is not spontaneous since ΔG > 0''')
        elif delta_g_sys == 0:
            print(f'''ΔG(system) is {delta_g_sys:.3f} (kJ/mol) 
The reaction is at equlibrium since ΔG = 0''')


def delta_g_calculator_using_uni():
    delta_uni = input(color.ORANGE + 'What is the ΔSuniv? \n' + color.END)
    delta_g_uni = -(298 * delta_uni)
    if delta_g_uni < 0:
        print(f'''ΔG(system) is {delta_g_uni:.5f} (kJ/mol) 
The reaction is spontaneous since ΔG < 0''')
    elif delta_g_uni > 0:
        print(f'''ΔG(system) is {delta_g_uni:.5f} (kJ/mol) 
The reaction is not spontaneous since ΔG > 0''')
    elif delta_g_uni == 0:
        print(f'''ΔG(system) is {delta_g_uni:.5f} (kJ/mol) 
The reaction is at equlibrium since ΔG = 0''')

