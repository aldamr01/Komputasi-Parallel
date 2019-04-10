def command(p1,p2,p3,p4):
    if p1 < p2 and p1 < p3 and p1 < p4 :
        return print('Rem mobil sekarang !') 
    elif p2 < p1 and p2 < p3 and p2 < p4 :
        return print('Rem mobil sekarang !')
    elif p3 < p1 and p3 < p2 and p3 < p4 :
        return print('Belok kanan sekarang !')
    elif p4 < p1 and p4 < p2 and p4 < p3 :
        return print('Belok kanan sekarang !')