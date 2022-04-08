# Delta G  = -(n)*F*Cell potential
#faraday constant = 96485 C/mol e-
# cell potential = J/C
# C = colomb
# Delta G Standard = -nFE
# Delta G > 0 -> E < 0
# Delta G < 0 -> E > 0
# Delta G = 0 -> E = 0

def delta_g_via_faraday_constant():
    moles_electrons = float(input('How many moles of electrons do you have? \n'))
    cell_potential = float(input('What is the cell potential \n'))
    faraday_constant = 96485
    delta_g = (-moles_electrons*cell_potential*faraday_constant)/1000
    print(f'{delta_g} kJ')
delta_g_via_faraday_constant()

