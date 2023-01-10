import variables

def co2_calculate(okul_mesafe, co2_type, kullanilan_aracta_kac_kisi): #co2_type için variables'deki CO2_LPG, CO2_benzin fln yazılacak. Eğer lpg benzin veya dizel seçilmişse özel araç kullanılır.
    if int(okul_mesafe) <= 5:
        variables.CO2_emisyon = 2.5 * co2_type / 100 / kullanilan_aracta_kac_kisi

    elif 5 < int(okul_mesafe) <= 10:
        variables.CO2_emisyon = 7.5 * co2_type / 100 / kullanilan_aracta_kac_kisi

    elif 10 < int(okul_mesafe) <= 15:
        variables.CO2_emisyon = 12.5 * co2_type / 100 / kullanilan_aracta_kac_kisi

    elif 15 < int(okul_mesafe) <= 20:
        variables.CO2_emisyon = 17.5 * co2_type / 100 / kullanilan_aracta_kac_kisi

    elif 20 < int(okul_mesafe) <= 25:
        variables.CO2_emisyon = 22.5 * co2_type / 100 / kullanilan_aracta_kac_kisi

    elif int(okul_mesafe) > 25:
        variables.CO2_emisyon = 30 * co2_type / 100 / kullanilan_aracta_kac_kisi

    print(variables.CO2_emisyon)


