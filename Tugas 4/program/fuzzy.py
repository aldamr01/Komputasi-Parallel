def command(p1,p2,p3,p4):
    if p3 == 0 :
        return print("NABRAK !!!!")
    elif p3 < 400 :
        return print("Kurangi kecepatan !!!") 
    elif p3 >400 and p3 <500 :
        return print("Belok ke kanan")
    

    if p2 <= 0 :
        return print("NABRAK !!!!")
    if p3 <= 0 :
        return print("NABRAK !!!!")
    if p4 <= 0 :
        return print("NABRAK !!!!")
        

    if p1 < p2 and p1 < p3 and p1 < p4 :
        return print('Rem mobil sekarang !') 
    elif p2 < p1 and p2 < p3 and p2 < p4 :
        return print('Rem mobil sekarang !')
    elif p3 < p1 and p3 < p2 and p3 < p4 :
        return print('Belok kanan sekarang !')
    elif p4 < p1 and p4 < p2 and p4 < p3 :
        return print('Belok kanan sekarang !')

    