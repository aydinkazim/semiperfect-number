print("Girilen aralıklar arasındaki yarı mükemmel sayıyı bulma")
min = int(input("Başlangıç: "))
max = int(input("Bitiş: "))

for i in range(min,max):
    bolenler = []
    for j in range(1,i-1):
        if (i % j == 0):
            bolenler.append(j)
    bolenler.reverse()
    toplam=0
    #burada diziyi "reverse()" ters çeviriyoruz ve ters çevrilmiş halindeli ilk 3 eleman ile "bolenler[0:3]" işlem yapıyoruz.
    #Yani yarı mükemmel sayı için bölenlerin en büyük 3 tanesini bulmuş oluyoruz.
    for x in range(0,len(bolenler[0:3])):
        toplam += bolenler[x]
    if(toplam == i):
        print("yarı mükemmel sayı: ",i)
