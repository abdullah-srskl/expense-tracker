import matplotlib.pyplot as plt

from data.data_manager import DataManager
from services.expense_service import ExpenseService


expenses = DataManager.load_expenses()
budget = DataManager.load_budget()


def menu_goster():
    print("\n--- Harcama Takip Uygulaması ---")
    print("1- Harcama ekle")
    print("2- Harcamaları listele")
    print("3- Toplam harcama")
    print("4- Kategoriye göre listele")
    print("5- Harcama sil")
    print("6- Harcama güncelle")
    print("7- Çubuk grafik göster")
    print("8- Pasta grafik göster")
    print("9- Aylık harcama")
    print("10- En yüksek harcama")
    print("11- Bütçe belirle")
    print("12- Çıkış")


def harcama_ekle():
    ad = input("Harcama adı: ")
    kategori = input("Kategori: ")

    while True:
        try:
            tutar = float(input("Tutar: "))

            if tutar < 0:
                print("Tutar negatif olamaz.")
                continue

            break
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

    expense = ExpenseService.create_expense(ad, tutar, kategori)

    expenses.append(expense)
    DataManager.save_expenses(expenses)

    print("Harcama başarıyla eklendi.")

    if ExpenseService.is_budget_exceeded(expenses, budget):
        print("⚠️ Bütçeyi aştın!")


def harcamalari_listele():
    if len(expenses) == 0:
        print("Henüz harcama yok.")
        return

    print("\n--- Harcamalar ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}- {expense.ad} - {expense.tutar} TL - "
            f"{expense.kategori} - {expense.tarih}"
        )


def toplam_harcama_goster():
    total = ExpenseService.get_total(expenses)
    print(f"Toplam harcama: {total} TL")


def kategoriye_gore_listele():
    kategori = input("Kategori gir: ")

    filtered_expenses = ExpenseService.filter_by_category(expenses, kategori)

    if len(filtered_expenses) == 0:
        print("Bu kategoride harcama bulunamadı.")
        return

    print(f"\n--- {kategori} Kategorisi ---")

    for expense in filtered_expenses:
        print(f"{expense.ad} - {expense.tutar} TL - {expense.tarih}")


def harcama_sil():
    if len(expenses) == 0:
        print("Silinecek harcama yok.")
        return

    harcamalari_listele()

    try:
        secim = int(input("Silmek istediğin harcama numarası: "))

        if secim < 1 or secim > len(expenses):
            print("Geçersiz numara.")
            return

        deleted_expense = expenses.pop(secim - 1)

        DataManager.save_expenses(expenses)

        print(f"{deleted_expense.ad} harcaması silindi.")

    except ValueError:
        print("Lütfen geçerli bir sayı gir.")


def harcama_guncelle():
    if len(expenses) == 0:
        print("Güncellenecek harcama yok.")
        return

    harcamalari_listele()

    try:
        secim = int(input("Güncellemek istediğin harcama numarası: "))

        if secim < 1 or secim > len(expenses):
            print("Geçersiz numara.")
            return

        expense = expenses[secim - 1]

        yeni_ad = input(f"Yeni ad ({expense.ad}): ")
        yeni_kategori = input(f"Yeni kategori ({expense.kategori}): ")

        while True:
            yeni_tutar = input(f"Yeni tutar ({expense.tutar}): ")

            if yeni_tutar == "":
                yeni_tutar = expense.tutar
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
            expense.ad = yeni_ad

        if yeni_kategori != "":
            expense.kategori = yeni_kategori

        expense.tutar = yeni_tutar

        DataManager.save_expenses(expenses)

        print("Harcama güncellendi.")

        if ExpenseService.is_budget_exceeded(expenses, budget):
            print("⚠️ Bütçeyi aştın!")

    except ValueError:
        print("Lütfen geçerli bir sayı gir.")


def cubuk_grafik_goster():
    categories = ExpenseService.group_by_category(expenses)

    if len(categories) == 0:
        print("Gösterilecek harcama yok.")
        return

    names = list(categories.keys())
    values = list(categories.values())

    plt.bar(names, values)
    plt.title("Kategoriye Göre Harcamalar")
    plt.xlabel("Kategori")
    plt.ylabel("Tutar (TL)")
    plt.show()


def pasta_grafik_goster():
    categories = ExpenseService.group_by_category(expenses)

    if len(categories) == 0:
        print("Gösterilecek harcama yok.")
        return

    names = list(categories.keys())
    values = list(categories.values())

    plt.pie(values, labels=names, autopct="%1.1f%%")
    plt.title("Kategoriye Göre Harcama Dağılımı")
    plt.show()


def aylik_harcama_goster():
    month = input("Ay gir (YYYY-MM): ")

    total = ExpenseService.get_monthly_total(expenses, month)

    print(f"{month} ayı toplam harcama: {total} TL")


def en_yuksek_harcama_goster():
    max_expense = ExpenseService.get_max_expense(expenses)

    if max_expense is None:
        print("Harcama yok.")
        return

    print(
        f"En yüksek harcama: {max_expense.ad} - "
        f"{max_expense.tutar} TL - {max_expense.kategori} - {max_expense.tarih}"
    )


def butce_belirle():
    global budget

    while True:
        try:
            new_budget = float(input("Bütçe miktarı: "))

            if new_budget < 0:
                print("Bütçe negatif olamaz.")
                continue

            budget = new_budget
            DataManager.save_budget(budget)

            print(f"Bütçe {budget} TL olarak ayarlandı.")
            break

        except ValueError:
            print("Lütfen geçerli bir sayı gir.")


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
        cubuk_grafik_goster()

    elif secim == "8":
        pasta_grafik_goster()

    elif secim == "9":
        aylik_harcama_goster()

    elif secim == "10":
        en_yuksek_harcama_goster()

    elif secim == "11":
        butce_belirle()

    elif secim == "12":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")