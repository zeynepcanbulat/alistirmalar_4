def kriptola():
    liste = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","a","b","c","d","e","f"] 
    print(len(liste))
    kripto = input("Cümleyi girin: " )
    kriptolanmış = []
    for n in range(0,len(kripto)):
        harf = kripto[n]
        x = liste.index(harf)
        liste[x] == liste[x+3]
        kriptolanmış.append(liste[x+3])
    print(kriptolanmış)
        
