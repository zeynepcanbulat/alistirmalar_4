from math import sqrt
liste = []
def sezarın_kutusu():
    a = input ("Cümleyi giriniz: ")
    x = len(a)
    while sqrt(x) != round(sqrt(x)):
        x = x+1
    print (sqrt(x))
    for i in range (0,round(sqrt(x))):
        for n in range(0,round(sqrt(x))):
            if n != round(sqrt(x)):
                kripto = a[i + round(sqrt(x))*n]
            liste.append(kripto)
    print(liste)
                
                
            
