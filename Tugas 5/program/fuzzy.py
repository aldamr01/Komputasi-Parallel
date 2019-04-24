def command(p1,p2,p3,p4,trafic):


    # if p3 == 0 :
    #     return print("NABRAK !!!!")
    # elif p3 < 400 :
    #     return print("Kurangi kecepatan !!!") 
    # elif p3 >400 and p3 <500 :
    #     return print("Belok ke kanan")
    

    # if p2 <= 0 :
    #     return print("NABRAK !!!!")
    # if p3 <= 0 :
    #     return print("NABRAK !!!!")
    # if p4 <= 0 :
    #     return print("NABRAK !!!!")
        

    if p1 < p2 and p1 < p3 and p1 < p4 :
        if trafic == 'merah' :
            print('Berhenti sekarang , lampu traffic lagi merah') 
        elif trafic == 'kuning' :
            print('Melaju pelan-pelan , lampu traffic lagi kuning') 
        else:
            if p1 <= 10 :
                print('Rem sekarang , didepan ada halangan') 
            elif p1 >= 10 and p1 < 20:
                print('Berjalan perlahan sekarang , didepan akan ada halangan') 
            elif p1 >= 50 :
                print('Melaju kedepan sekarang') 

    elif p2 < p1 and p2 < p3 and p2 < p4 :       
        if p2 <= 10 :
            print('Rem sekarang , dibelakang ada halangan') 
        elif p2 >= 10 and p2 < 20:
            print('mundur perlahan sekarang , awas dibelakang akan ada halangan') 
        elif p2 >= 50 :
            print('Mundur kebelakang')

    elif p3 < p1 and p3 < p2 and p3 < p4 :
        if trafic == 'merah' :
            print('Berhenti sekarang , lampu traffic lagi merah') 
        elif trafic == 'kuning' :
            print('Melaju pelan-pelan , lampu traffic lagi kuning') 
        else:
            if p3 <= 10 :
                print('Belok ke kanan sekarang , disamping akan menabrak') 
            elif p3 >= 10 and p3 < 20:
                print('Belok nya pelan pelan , disamping akan ada halangan') 
            elif p3 >= 50 :
                print('Silahkan belok ke kiri bebas , tidak ada halangan terdeteksi') 

    elif p4 < p3 and p4 < p2 and p4 < p1 :
        if trafic == 'merah' :
            print('Berhenti sekarang , lampu traffic lagi merah') 
        elif trafic == 'kuning' :
            print('Melaju pelan-pelan , lampu traffic lagi kuning') 
        else:
            if p3 <= 10 :
                print('Belok ke kiri sekarang , disamping akan menabrak') 
            elif p3 >= 10 and p3 < 20:
                print('Belok nya pelan pelan , disamping akan ada halangan') 
            elif p3 >= 50 :
                print('Silahkan belok ke kanan bebas , tidak ada halangan terdeteksi') 
    