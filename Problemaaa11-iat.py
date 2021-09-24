n=int(input('Dati numarul de elemente din vector='))
if 0 < n < 10:  
    a=[]
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
    print(a)
    print('a) afişează pe ecran componentele tabloului la un interval de 5 poziţii',a[::5])
    print('b) afişează pe ecran numerele în ordinea inversă a introducerii în calculator',a[::-1])
    c=sorted(a)
    c.sort(reverse=True)
    print('c)  sortează componentele tabloului în ordine descrescătoare',c)
    pare=[]
    for i in range(0,len(a)):
        if a[i]%2==0:
            k=a[i]
            pare.extend([k])
    print('d)  afişează pe ecran doar componentele pare',pare)
    print('e)  afişează pe ecran media aritmetică a componentelor pare', (sum(pare)/len(pare)))
    
    impare=[]
    for i in range(0,len(a)):
        if a[i]%2!=0:
            im=a[i]
            impare.extend([im])
    print('f)  afişează pe ecran doar componentele impare;',impare)
    
    x=int(input("x="))
    y=int(input("y="))
    dm=[]
    for i in a:
        if ((i>x)and(i%y!=0)):
            z=i
            dm.extend([z])
    print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y :',dm)
    marimici=[]
    for i in a:
        if ((i>x)and(i<y)):
            y=i
            marimici.extend([y])
    print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y :',marimici)
    negative=[]
    for i in impare:
        if i<0:
            negative.extend([a.index(i)])
    print('i)  afişează pe ecran poziţiile componentelor impare negative:',negative)
    douacif=[]
    for i in range(0,n):
        if ((a[i]>9)and(a[i]<100))or((a[i]>-100)and(a[i]<-9)):
            douacif.extend([i])
    print('j)  afişează pe ecran poziţiile componentelor ce conţin doar două cifre semnificative:',douacif)
    minim=a.copy()
    minim[0]=min(minim)
    print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv:',minim)
    prim=a.copy()
    prim[prim.index(min(prim))]=prim[0]
    print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia:',prim)
    print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură:')
    print('p=',pare)
    print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
    div3=[]
    for i in range(0,len(a)):
        if a[i]%3==0:
            y=a[i]
            div3.extend([y])
    print('d=',div3)
    print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori;')
    d = []
    for i in a:
        divizori = []
        for j in range (1, i + 1):
            if i % j == 0:
                divizori.append(j)
        if 1 <= len(divizori) <= 4:
            d.append(i)  
    print(d)               
else:
    print("Numarul de elemente nu corespunde cerintelor")    
    