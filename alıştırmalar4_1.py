from math import sqrt
liste = []
def sezarın_kutusu():
    string = input ("Cümleyi giriniz: ")
    a = list(string)
    x = len(a)
    
    while sqrt(x) != round(sqrt(x)):
        x = x+1

    print(x)
    
    fark = x - len(a) #n*n matris olmadığında problem yaşamayalım diye
    print(fark)
    for k in range(0,fark):
        a.append(" ")
    print(a)
    
    for i in range (0,round(sqrt(x))):
        for n in range(0,round(sqrt(x))):
            if n != round(sqrt(x)):
                kripto = a[i + round(sqrt(x))*n]
            liste.append(kripto)
    print(liste)
liste = []
