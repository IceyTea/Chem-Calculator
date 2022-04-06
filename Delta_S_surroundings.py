import Standard_entropy_calculator
import Standard_enthalpy_formation
import Temperature_calculator

def ssurroundings():
    global surroundings
    surroundings = -(Standard_enthalpy_formation.delta_h_final / Temperature_calculator.temp_value)
    print(f'Your Delta S Surroundings is {surroundings:.7f} kJ/K')

def suniverse():
    global surroundings
    global universe
    question = input(f'Do you want S Universe in J or kJ?\n ')
    question = question.lower()
    if question == "j":
        universe = Standard_entropy_calculator.delta_s_final + (surroundings * 1000)
        print(universe)
    
        if universe > 0:
            print(f'''Your Delta S Universe is {universe:.3f} J/K
            The reaction is spontaneous''')
        elif universe < 0:
            print(f'''Your Delta S Universe is {universe:.3f} J/K
            The reaction is not spontaneous''')
        elif universe == 0:
            print(f'''Your Delta S Universe is {universe:.3f} J/K
            The reaction is at equilibrium''')
    
    elif question == "kj":
        universe = float(Standard_entropy_calculator.delta_s_final / 1000) + float(ssurroundings)
        if universe > 0:
            print(f'''Your Delta S Universe is {universe:.3f} kJ/K 
            The reaction is spontaneous since ΔSuni > 0''')
        elif universe < 0:
            print(f'''Your Delta S Universe is {universe:.3f} kJ/K
            The reaction is not spontaneous since ΔSuni < 0 ''')
        elif universe == 0:
            print(f'''Your Delta S Universe is {universe:.2f} kJ/K
            The reaction is at equilibrium since ΔSuni = 0''')


        