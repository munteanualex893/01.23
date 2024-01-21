'''
Să se scrie toate prefixele unui cuvânt dat; prin prefix se înţelege şirul format din primele
caractere ale cuvântului, minim un caracter, maxim toate. Exemplu: prefixele pentru
tablou sunt: t ta tab tabl tablo tablou.'''
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex3/Text_intrare', 'r') as f:
    a=f.read()
    b=len(a)+1
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex3/Text_iesire', 'w') as f:
    for i in range (0,b,1):
        f.write(a[:i]+'  ')