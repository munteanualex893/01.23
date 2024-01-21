'''
Să se afişeze toate sufixele unui cuvânt. Exemplu: cuvântul tablou, sufixele: u ou lou
blou ablou tablou.'''
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex4/Text_intrare', 'r') as f:
    a=f.read()
    b=len(a)+1
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex4/Text_iesire', 'w') as f:
    for i in reversed(range (0,b,1)):
        f.write(a[:i]+'  ')