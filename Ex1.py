'''
Să se afişeze cu litere mari un text dat, de maxim 255 caractere. Exemplu: Date de
intrare text: Cerc dE InfO Date de ieşire CERC DE INFO.'''
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex1/Text_intrare','r') as f:
    a=f.read()
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex1/Text_iesire','w') as f:
    f.write(a.upper()) 