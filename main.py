import json
import matplotlib.pyplot as plt

harcamalar = []


def menu_goster():
    print("\n--- Harcama Takip Uygulaması ---")
    print("1- Harcama ekle")
    print("2- Harcamaları listele")
    print("3- Toplam harcama")
    print("4- Kategoriye göre harcamaları listele")
    print("5- Harcama sil")
    print("6- Harcama Güncelleme")
    print("7- Grafik göster")
    print("8- Pasta grafik göster")
    print("9- Çıkış")

def verileri_kaydet():
    with open("harcamalar.json", "w", encoding="utf-8") as dosya:
        json.dump(harcamalar, dosya, ensure_ascii=False, indent=4)


def verileri_yukle():
    global harcamalar

    try:
        with open("harcamalar.json", "r", encoding="utf-8") as dosya:
            harcamalar = json.load(dosya)
    except FileNotFoundError:
        harcamalar = []


def harcama_ekle():
    ad = input("Harcama adı: ")
    kategori = input("Kategori: ")

    while True:
        try:
            tutar = float(input("Tutar: "))
            if tutar < 0:
                print("Tutar negatif olamaz!")
                continue
            break
        except ValueError:
            print("Hatalı giriş! Lütfen sayı gir.")

    harcama = {
        "ad": ad,
        "tutar": tutar,
        "kategori": kategori
    }

    harcamalar.append(harcama)
    verileri_kaydet()
    print("Harcama eklendi.")


def harcama_sil():
    if len(harcamalar) == 0:
        print("Silinecek harcama yok.")
        return

    print("\n--- Harcamalar ---")

    for index, harcama in enumerate(harcamalar, start=1):
        print(f"{index}- {harcama['ad']} - {harcama['tutar']} TL - {harcama['kategori']}")

    try:
        secilen = int(input("Silmek istediğin harcama numarası: "))

        if secilen < 1 or secilen > len(harcamalar):
            print("Geçersiz numara.")
            return

        silinen = harcamalar.pop(secilen - 1)
        verileri_kaydet()

        print(f"{silinen['ad']} harcaması silindi.")

    except ValueError:
        print("Lütfen geçerli bir sayı gir.")

def harcama_guncelle():
    if len(harcamalar) == 0:
        print("Güncellenecek harcama yok.")
        return

    print("\n--- Harcamalar ---")

    for index, harcama in enumerate(harcamalar, start=1):
        print(f"{index}- {harcama['ad']} - {harcama['tutar']} TL - {harcama['kategori']}")

    try:
        secilen = int(input("Güncellemek istediğin harcama numarası: "))

        if secilen < 1 or secilen > len(harcamalar):
            print("Geçersiz numara.")
            return

        harcama = harcamalar[secilen - 1]

        yeni_ad = input(f"Yeni ad ({harcama['ad']}): ")
        yeni_kategori = input(f"Yeni kategori ({harcama['kategori']}): ")

        while True:
            yeni_tutar = input(f"Yeni tutar ({harcama['tutar']}): ")

            if yeni_tutar == "":
                yeni_tutar = harcama["tutar"]
                break

            try:
                yeni_tutar = float(yeni_tutar)

                if yeni_tutar < 0:
                    print("Tutar negatif olamaz.")
                    continue

                break
            except ValueError:
                print("Lütfen geçerli bir sayı gir.")

        if yeni_ad != "":
            harcama["ad"] = yeni_ad

        if yeni_kategori != "":
            harcama["kategori"] = yeni_kategori

        harcama["tutar"] = yeni_tutar

        verileri_kaydet()
        print("Harcama güncellendi.")

    except ValueError:
        print("Lütfen geçerli bir sayı gir.")



def harcamalari_listele():
    if len(harcamalar) == 0:
        print("Henüz harcama yok.")
    else:
        print("\n--- Harcamalar ---")

        for harcama in harcamalar:
            print(f"{harcama['ad']} - {harcama['tutar']} TL - {harcama['kategori']}")


def toplam_harcama_goster():
    toplam = 0

    for harcama in harcamalar:
        toplam += harcama["tutar"]

    print(f"Toplam harcama: {toplam} TL")

def kategoriye_gore_listele():
    if len(harcamalar) == 0:
        print("Henüz harcama yok.")
        return

    aranan_kategori = input("Hangi kategoriyi listelemek istiyorsun?: ")

    bulundu_mu = False

    print(f"\n--- {aranan_kategori} Kategorisindeki Harcamalar ---")

    for harcama in harcamalar:
        if harcama["kategori"].lower() == aranan_kategori.lower():
            print(f"{harcama['ad']} - {harcama['tutar']} TL - {harcama['kategori']}")
            bulundu_mu = True

    if bulundu_mu == False:
        print("Bu kategoride harcama bulunamadı.")


def grafik_goster():
    if len(harcamalar) == 0:
        print("Gösterilecek harcama yok.")
        return

    kategoriler = {}

    for harcama in harcamalar:
        kategori = harcama["kategori"]
        tutar = harcama["tutar"]

        if kategori in kategoriler:
            kategoriler[kategori] += tutar
        else:
            kategoriler[kategori] = tutar

    isimler = list(kategoriler.keys())
    degerler = list(kategoriler.values())

    plt.bar(isimler, degerler)
    plt.title("Kategoriye Göre Harcamalar")
    plt.xlabel("Kategori")
    plt.ylabel("Tutar (TL)")
    plt.show()


def pasta_grafik_goster():
    if len(harcamalar) == 0:
        print("Gösterilecek harcama yok.")
        return

    kategoriler = {}

    for harcama in harcamalar:
        kategori = harcama["kategori"]
        tutar = harcama["tutar"]

        if kategori in kategoriler:
            kategoriler[kategori] += tutar
        else:
            kategoriler[kategori] = tutar

    isimler = list(kategoriler.keys())
    degerler = list(kategoriler.values())

    plt.pie(degerler, labels=isimler, autopct="%1.1f%%")
    plt.title("Kategoriye Göre Harcama Dağılımı")
    plt.show()

verileri_yukle()

while True:
    menu_goster()
    secim = input("Seçiminiz: ")

    if secim == "1":
        harcama_ekle()

    elif secim == "2":
        harcamalari_listele()

    elif secim == "3":
        toplam_harcama_goster()

    elif secim == "4":
        kategoriye_gore_listele()

    elif secim == "5":
        harcama_sil()

    elif secim == "6":
        harcama_guncelle()

    elif secim == "7":
        grafik_goster()

    elif secim == "8":
        pasta_grafik_goster()

    elif secim == "9":
        print("Programdan çıkılıyor...")
        break