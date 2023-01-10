#Istanbul Köy Hizmetleri Anadolu Lisesi
# Tubitak 2204A Projesi
#Ayfer Kilicoglu danismanliginda Sila Beril Olcay
#Aralik 2022

#Bu çalisma kapsaminda benzinli, dizel araclar ile otobus ve metro gibi toplu tasima kullaniminda ortaya cikan CO2 emisyon degerleri
#Devin Bahceci nin Kisisel karbon ayak izi rehberi kitabinin 31 ve 37 nolu sayfalari arasinda bulunan hesaplamalar ve tablolardan elde edilmistir.

arac = None
arac_yakit = None
okul_ev_mesafe = None

co2emisyon_sinif9 = None
co2_emisyon_10 = None
co2_emisyon_11 = None
co2_emisyon_12 = None

co2_emisyon_sinif9_gunluk = 0
co2_emisyon_sinif10_gunluk = 0
co2_emisyon_sinif11_gunluk = 0
co2_emisyon_sinif12_gunluk = 0

number_of_students_sinif_9 = 0
number_of_students_sinif_10 = 0
number_of_students_sinif_11 = 0
number_of_students_sinif_12 = 0

co2_emisyon = None

CO2_benzin = 17.3 # kisinin seyahat ettigi 1.6 litre benzinli araç 100 kmde 17.3 kg CO2 emisyonu
CO2_LPG = 17.3 # LPG benzin ile karsilastirildiginda %25 daha fazla kullanildigi için CO2 emisyon degeri benzin ile ayni kabul edilmistir
CO2_dizel = 12.9 #2 kisinin seyahat ettigi 1.6 litre dizel araç 100 kmde 12.9 kg CO2 emisyonu
CO2_otobus = 8.9 #Otobüs 100 kmde ortalama kisi basi 8.9 kg CO emisyonu
CO2_okul_servisi =  2.31 #Okul servisi 1 kmde 0.15 litre dizel yakiyorsa 100 kmde 15 litre yakar. 15 litre * 2.772 kgCO2/litre / 18 kisi = 2.31 kg CO2 / kisi
CO2_minibus = 2.618 #Minibus 1 kmde 0.17 litre dizel yakiyorsa 100 kmde 17 litre yakar. 17 litre * 2.772 kgCO2/litre / 18 kisi = 2.618 kg CO2 / kisi
CO2_metro = 5.3 #Metro 100 kmde ortalama kisi basi 5.3 kg CO emisyonu

#------------------------------------------------------------------------------------

CO2_emisyon = 0 #Her bir grup için hesaplanabilmesi amaciyla burada sifirlanmistir.





