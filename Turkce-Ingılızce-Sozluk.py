def kelimeEkleme() :

	dosya = open("sozluk.dat","a")

	m = raw_input("Turkce kelimeyi giriniz: ")
	h = raw_input("Ingilizce karsiligini girin: ")

	satir = m + "\t"+ ":" + "\t" + h + "\n"

	dosya.write(satir)
	dosya.close()

def ingGuncelle() :

	dosya = open("sozluk.dat","r")

	istek = raw_input("Guncelleme yapacaginiz kelimeyi yaziniz: ")

	satirlar = dosya.readlines()
	
	dizi = []
	for i in range(len(satirlar)) :
		
		sonraki = satirlar[i]
		guncelleme = sonraki.find(istek)

		if guncelleme != -1 :
			a = istek
			b = raw_input("yeni ingilizce ceviriyi girin: ")
			
			yeni = a +"\t" + ":" + "\t" + b + "\n"
			dizi.append(yeni)
		
		else :
			dizi.append(sonraki)	
	dosya.close()

	dosya = open("sozluk.dat","w")

	dosya.writelines(dizi)
	dosya.close()

def sorgulama() :

	dosya = open("sozluk.dat","r")

	aranan = raw_input("Ingilizce anlamini istediginiz kelimeyi giriniz: ")

	ara = dosya.readlines()

	for i in range(len(ara)) :

		siradaki = ara[i]
		bulunan = siradaki.find(aranan)
		
		if bulunan != -1 :
			print ara[i]

	dosya.close()

def listeleme() :

	dosya = open("sozluk.dat","r")

	harf = raw_input("Hangi harf ile baslayanlari listelemek istiyorsunuz: ")
	bulunacak = dosya.readlines()

	for i in range(len(bulunacak)) :

		gelecek = bulunacak[i]
		liste = gelecek.find(harf)

		if liste == 0 :
			print bulunacak[i]
	dosya.close

def kelimeList() :
	
	dosya = open("sozluk.dat","r")

	kelime = raw_input("Hangi kelimenin gececegini yaziniz: ")

	arama = dosya.readlines()

	for i in range(len(arama)) :

		kelimeler = arama[i]
		ayrilmis = kelimeler.split("\t")
		ayrik = ayrilmis[0].find(kelime)

		if ayrik != -1 :
			print arama[i]
	dosya.close()

def turkceAyir() :

	dosya = open("sozluk.dat","r")

	turkce = dosya.readlines()
	
	dizi = []
	for i in range(len(turkce)) :
		
		ayir = turkce[i]
		ayrilacak = ayir.split("\t")
		atanacak = ayrilacak[0] +"\n"
		dizi.append(atanacak)

	dosya.close()

	dosya = open("turkce_kelimeler.dat","w")

	dosya.writelines(dizi)
	dosya.close() 

def tumListe() :

	dosya = open("sozluk.dat","r")

	tum = dosya.readlines()

	for i in range(len(tum)) :

		print i+1,"-",tum[i]

def turkGuncel() :

	dosya = open("sozluk.dat","r")

	ing = raw_input("Turkcesi degistirilcek kelimeyi girin: ")

	liste = dosya.readlines()
	dizi = []
	
	for i in range(len(liste)) :

		sonraki = liste[i]
		ayir = sonraki.split("\t")
		bulundu = ayir[0] 
		degistir = sonraki.find(ing)


		if degistir != -1 :
			a = ayir[2] 
			b = raw_input("yeni turkce kelimeyi girin: ")
			
			yeni = b + "\t" + ":" + "\t" + a  
			dizi.append(yeni)
		else :
			dizi.append(sonraki)
		
	dosya.close()
	
	dosya = open("sozluk.dat","w")

	dosya.writelines(dizi)
	dosya.close()
	
		


print "\t","\t","MENU"
print "1.Sozluge Yeni Kelime Ekleme"
print "2.Sozlukteki Bir Kelimenin Ingilizce Anlamini Guncelleme"
print "3.Sozlukteki Bir Kelimenin Ingilizce Anlamini Sorgulama"
print "4.Girilen Bir Harf Ile Baslayan Kelimeler Ve Ingilizce Anlamlarinin Listelenmesi"
print "5.Girilen Bir Metin Parcasinin gectigi kelimeler ve Anlamlarinin Listesi"
print "6.Turkce Kelimeleri Baska Dosyaya At"
print "7.Tum Kelimeleri Listele"
print "8.Turkce Kelime Guncelleme"

secim = input("Gormek istediginiz secenegi giriniz: ")

if secim == 1 :
	kelimeEkleme()

elif secim == 2 :
	ingGuncelle()

elif secim == 3 :
	sorgulama()

elif secim == 4 :
	listeleme()

elif secim == 5 :
	kelimeList()

elif secim == 6 :
	turkceAyir()

elif secim == 7 :
	tumListe()

elif secim == 8 :
	turkGuncel()
