import datetime



def is_resmi_tatil(tarih):
    tatiller = [
        datetime.date(2024, 4, 8),
        datetime.date(2024, 4, 9),
        datetime.date(2024, 4, 10),
        datetime.date(2024, 4, 11),
        datetime.date(2024, 4, 12),
        datetime.date(2024, 4, 23),
        datetime.date(2024, 5, 1),
        datetime.date(2024, 6, 17),
        datetime.date(2024, 6, 18),
        datetime.date(2024, 6, 19),
        datetime.date(2024, 6, 20),
        datetime.date(2024, 6, 21),
        datetime.date(2024, 7, 15),
        datetime.date(2024, 8, 30),
        datetime.date(2024, 10, 28),
        datetime.date(2024, 10, 29),

        datetime.date(2023, 8, 30),
        datetime.date(2023, 6, 28),
        datetime.date(2023, 6, 29),
        datetime.date(2023, 6, 30),
        datetime.date(2023, 5, 19),
        datetime.date(2023, 5, 1),
        datetime.date(2023, 4, 21),
        datetime.date(2023, 4, 22),
        datetime.date(2023, 4, 23),

        datetime.date(2022, 8, 30),
        datetime.date(2022, 7, 11),
        datetime.date(2022, 7, 12),
        datetime.date(2022, 7, 15),
        datetime.date(2022, 5, 2),
        datetime.date(2022, 5, 3),
        datetime.date(2022, 5, 4),
        datetime.date(2022, 5, 19),

        datetime.date(2021, 10, 29),
        datetime.date(2021, 8, 30),
        datetime.date(2021, 1, 1),
        datetime.date(2021, 4, 23),
        datetime.date(2021, 5, 13),
        datetime.date(2021, 5, 14),
        datetime.date(2021, 5, 15),
        datetime.date(2021, 5, 19),
        datetime.date(2021, 7, 15),
        datetime.date(2021, 7, 20),
        datetime.date(2021, 7, 21),
        datetime.date(2021, 7, 22),
        datetime.date(2021, 7, 23),
        datetime.date(2021, 8, 30),

        datetime.date(2019, 1, 1),
        datetime.date(2019, 4, 23),
        datetime.date(2019, 5, 1),
        datetime.date(2019, 6, 4),
        datetime.date(2019, 6, 5),
        datetime.date(2019, 6, 6),
        datetime.date(2019, 6, 7),
        datetime.date(2019, 7, 15),
        datetime.date(2019, 8, 12),
        datetime.date(2019, 8, 13),
        datetime.date(2019, 8, 14),
        datetime.date(2019, 8, 15),
        datetime.date(2019, 8, 16),
        datetime.date(2019, 8, 30),
        datetime.date(2019, 10, 29)
    ]
    return tarih in tatiller

def hesapla_tarih(tarih_str):
    try:
        tarih = datetime.datetime.strptime(tarih_str, "%d/%m/%Y")
        tarih += datetime.timedelta(days=16)

        while is_resmi_tatil(tarih.date()) or tarih.weekday() in [5, 6]:
            tarih += datetime.timedelta(days=2)
        if tarih.weekday() == 0:  # Pazartesi gününe denk geliyorsa
            tarih += datetime.timedelta(days=1)  # 1 gün ekleyerek kesinleşme tarihini belirle
        elif tarih.weekday() == 5:  # Cumartesi gününe denk geliyorsa
            tarih += datetime.timedelta(days=3)  # 3 gün ekleyerek kesinleşme tarihini belirle
        elif tarih.weekday() == 6:  # Pazar gününe denk geliyorsa
            tarih += datetime.timedelta(days=2)  # 2 gün ekleyerek kesinleşme tarihini belirle
        elif is_resmi_tatil(tarih.date()):  # Tatillere denk geliyorsa
            tarih += datetime.timedelta(days=2)  # Tatilin ardından 2 gün ekleyerek kesinleşme tarihini belirle

        return tarih.strftime("KESİNLEŞTİRME TARİHİ      : %d/%m/%Y")
    except ValueError:
        return "Geçersiz tarih formatı. Lütfen GÜN/AY/YIL biçiminde girin."


while True:
    tarih_girisi = input("TEBLİĞ TARİHİ (GÜN/AY/YIL): ").replace("/", "").strip()
    tarih_girisi = f"{tarih_girisi[:2]}/{tarih_girisi[2:4]}/{tarih_girisi[4:]}"
    sonuc = hesapla_tarih(tarih_girisi)
    print(sonuc)
    print("")
