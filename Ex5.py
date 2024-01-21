'''
Să se codifice un text dat afişând în locul fiecărei litere codul ei ASCII. Să se afişeze
textul codificat, cu un spaţiu între coduri şi trei spaţii pentru un spaţiu în text. Exemplu:
textul: Am un mar se va afişa 65 109 117 110 109 97 114.'''
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex5/Text_intrare', 'r') as f:
    a=f.read()
    b=len(a)+1
with open('E:/Alexandru/Scoala/Tema_pentru_acasa/01.23/Ex5/Text_iesire', 'w') as f:
    for i in range (0,b,1):
        c=str(a[i])
        d=str(ord(c))
        f.write(d+'  ')