class Expense:
    def __init__(self, ad, tutar, kategori, tarih):
        self.ad = ad
        self.tutar = tutar
        self.kategori = kategori
        self.tarih = tarih

    def to_dict(self):
        return {
            "ad": self.ad,
            "tutar": self.tutar,
            "kategori": self.kategori,
            "tarih": self.tarih
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["ad"],
            data["tutar"],
            data["kategori"],
            data.get("tarih", "Tarih yok")
        )