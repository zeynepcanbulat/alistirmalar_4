from math import sqrt
def sezar_geliştir():
    liste = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
    listeen=[]
    liste_index =[]
    
    anahtar = input("Anahtar kelimeyi giriniz: ")
    kriptola = input("Kriptolanacak kelimeyi giriniz: ")
    a = list(kriptola)
    x = len(anahtar)
     
    fark = x*x - len(a) #n*n matris olmadığında problem yaşamayalım diye
    print(fark)       #boşluk ekleyerek n*ne tamamlıyoruz

    for k in range(0,fark):
        a.append(" ")
    print(a)

    for n in range(0,len(anahtar)):
        harf = anahtar[n]
        index = liste.index(harf)
        liste_index.append(index)

    for i in range(0,len(kriptola),x):
        listeen.append(kriptola[i : i+x]) #listenin devamı yok şuanlık 
    print(listeen)

    #for y in range(0,x):
     #   min_liste = min(liste_index)
      #  indeex = liste_index.index(min_liste)
       # print(listeen[indeex])
        #liste_index.remove(min_liste)
        

        
    
        
        
        
        
        
        
        
            
        
        
        
        
            
        

