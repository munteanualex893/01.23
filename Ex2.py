'''Să se afişeze numărul de vocale dintr-un text scris cu litere mici, memorat într-o
variabilă string.
'''
c = 0
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex2/Text_intrare', 'r') as f:
    a = f.read()
for i in a:
    if ord(i) in [97, 101, 105, 111, 117]:
        c += 1
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex2/Text_iesire', 'w') as f:
    f.write(str(c))