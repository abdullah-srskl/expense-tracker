# Expense Tracker

Python ile geliştirilmiş, nesne yönelimli (OOP) ve katmanlı mimari kullanan kişisel harcama takip uygulaması.

## Özellikler

- Harcama ekleme
- Harcamaları listeleme
- Toplam harcama görüntüleme
- Kategoriye göre filtreleme
- Harcama silme
- Harcama güncelleme
- Tarih bazlı harcama kaydı
- Aylık harcama raporu
- En yüksek harcamayı görüntüleme
- Bütçe belirleme ve bütçe aşım uyarısı
- Kategoriye göre çubuk grafik
- Kategoriye göre pasta grafik
- JSON ile veri saklama
- Modüler ve katmanlı proje yapısı

## Proje Mimarisi

```text
expense-tracker/
│
├── main.py
│
├── models/
│   └── expense.py
│
├── services/
│   └── expense_service.py
│
├── data/
│   └── data_manager.py
│
├── harcamalar.json
├── settings.json
├── requirements.txt
└── README.md
```

### Katmanlar

#### Model Layer

Harcama nesnesinin yapısını tanımlar.

```python
class Expense
```

#### Service Layer

İş mantığını içerir.

- Toplam harcama hesaplama
- En yüksek harcama bulma
- Kategori filtreleme
- Aylık raporlama
- Bütçe kontrolü

#### Data Layer

JSON dosyalarına veri kaydetme ve yükleme işlemlerini yönetir.

#### UI Layer

Kullanıcı ile etkileşimi sağlar.

```python
main.py
```

## Kullanılan Teknolojiler

- Python
- Object Oriented Programming (OOP)
- JSON
- Matplotlib
- Git
- GitHub

## Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/abdullah-srskl/expense-tracker.git
```

Proje klasörüne girin:

```bash
cd expense-tracker
```

Gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

Programı çalıştırın:

```bash
python main.py
```

## Ekran Görüntüleri

### Pasta Grafik

![Pasta Grafik](screenshots/pie-chart.png)

### Çubuk Grafik

![Çubuk Grafik](screenshots/bar-chart.png)

## Öğrenilen Konular

Bu proje geliştirilirken aşağıdaki konular uygulanmıştır:

- Değişkenler
- Fonksiyonlar
- Döngüler
- Koşullar
- Hata Yönetimi
- JSON İşlemleri
- Veri Modelleme
- Nesne Yönelimli Programlama (OOP)
- Katmanlı Mimari
- Veri Görselleştirme
- Git
- GitHub

## Gelecek Planları

- Flask ile web arayüzü
- SQLite veritabanı desteği
- Kullanıcı hesabı sistemi
- Dashboard ekranı
- PDF rapor çıktısı
- REST API geliştirme