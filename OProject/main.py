import variables
import algorithm

print("UYARI:sayı girdiginizden emim olun\n")

kullanilan_aracta_kac_kisi = None
okul_mesafe = int(input("okul-ev arası mesafe? \n"))
arac_turu = int(input("araç türü?\n ozel araç kullanıyorsanız 1'e, otobus kullanıyorsanız 2'yi, minibus kullanıyorsanız 3'u, okul servisi kullanıyorsanız 4'u, metro kullanıyorsanız 5'i gitiniz\n"))

while True:
    if arac_turu == 1:
        yakıt_turu = int(input("yakıt türü?\n benzin kullanıyorsanız 1'i, lpg kullanıyorsanız 2'yi, dizel kullanıyorsanız 3'ü giriniz.\n"))
        if yakıt_turu == 1:
            co2_type = variables.CO2_benzin
            kullanilan_aracta_kac_kisi = 2
        elif yakıt_turu == 2:
            co2_type = variables.CO2_LPG
            kullanilan_aracta_kac_kisi = 2
        elif yakıt_turu == 3:
            co2_type = variables.CO2_dizel
            kullanilan_aracta_kac_kisi = 2
        else:
            print("lütfen sadece bahsedilen sayıları kullanın\n")
            exit()
        break
    elif arac_turu == 2:
        co2_type = variables.CO2_otobus
        kullanilan_aracta_kac_kisi = 1
        break
    elif arac_turu == 3:
        co2_type = variables.CO2_minibus
        kullanilan_aracta_kac_kisi = 1
        break
    elif arac_turu == 4:
        co2_type = variables.CO2_okul_servisi
        kullanilan_aracta_kac_kisi = 1
        break
    elif arac_turu == 5:
        co2_type = variables.CO2_metro
        kullanilan_aracta_kac_kisi = 1
        break
    else:
        print("lütfen sadece bahsedilen sayıları kullanın\n")
        exit()

algorithm.co2_calculate(okul_mesafe=okul_mesafe, co2_type=co2_type, kullanilan_aracta_kac_kisi=kullanilan_aracta_kac_kisi)