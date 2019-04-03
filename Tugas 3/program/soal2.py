list = [1,2,3,4,5,6,7,8,9,10]

def kuadrat(x):
    for i in range(len(list)):
        list[i] = list[i]*list[i]
    print(list)

kuadrat(list)