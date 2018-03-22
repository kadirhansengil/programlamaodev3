# programlamaodev3

Soru-1)
satis=500
fiyat=20
ciro=5000
i=1
while True:
    satis=satis+200
    fiyat=fiyat+10
    ciro=ciro+(satis*fiyat)
    i=i+1
    if (ciro>500000):
        print(i,"Ay sonra cironuz",ciro,"olur.500.000 üzerine çıkar.")
        break
        
        
Soru-2)
stok=10000
i=1
while True:
    stok=stok-400
    i=i+1
    if (stok<=0):
        print(i,"Ay Sonra Stoklarınız Sıfırlanır:")
        break
        
        
Soru-3)

girilen=""
while (girilen!="0"):
    girilen=input("Bir sayı giriniz. Çıkış için [0]")
    if girilen=="0":
        print("Program sonlandırıldı.")
    else:
        girilen=float(girilen)
        print("Girdiğiniz sayının 3 ile bölümünden kalan:",girilen%3)
        
        
        
Soru-4)
saat=1
while(saat>0):
    saat=int(input("Haftalık Personel Çalışma Saati Giriniz:"))
    if(saat>62):
        print("Haftalık 22 Saatten Fazla Mesai Yapılamaz!")
        break
        
    mesai=saat-40
    omaas=40*90+(mesai*9)
    print("Ödenecek Maaş=",omaas)
    
    
Soru-5)
gunUretim=200
gunDefoluUrun=0
topDefoluUrun=0
i=0
while (gunDefoluUrun<=gunUretim*0.20):
    gunDefoluUrun=int(input("Günlük Defolu Ürün Sayısı:"))
    topDefoluUrun=topDefoluUrun+gunDefoluUrun
    i=i+1
    if (gunDefoluUrun>gunUretim*0.20):
        print("Defolu Ürün Sayısı Limiti Aştı.")
        break
    print(i,"Günlük","Defolu Ürün Sayısı",topDefoluUrun)


