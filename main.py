from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox

veriler = [
    ("Masif Ahşap", 1.30),
    ("Tutkallı Lamine Ahşap", 1.25),
    ("Lamine Levha Ahşap LVL, Kontrplak, OSB", 1.20),
    ("Yonga Levhalar", 1.30),
    ("Lif Levhaları, sert", 1.30),
    ("Lif Levhaları, orta", 1.30),
    ("Lif Levhaları, MDF", 1.30),
    ("Lif Levhaları, yumuşak", 1.30),
    ("Çapraz Lamine Ahşap, CLT", 1.30),
    ("Birleşimler", 1.30),
    ("Delikli Metal Plaka Bağlantı Elemanları", 1.25),
    ("Kazara Oluşan Tasarım Durumu", 1.00)
]

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tablo Örnek")
        layout = QVBoxLayout(self)

        self.tablo = QTableWidget()
        self.tablo.setColumnCount(2)
        self.tablo.setHorizontalHeaderLabels(["Malzeme", "Katsayı"])
        self.tablo.setRowCount(len(veriler))
        layout.addWidget(self.tablo)

        # Satır ekleme
        for i, (ad, katsayi) in enumerate(veriler):
            self.tablo.setItem(i, 0, QTableWidgetItem(ad))
            self.tablo.setItem(i, 1, QTableWidgetItem(str(katsayi)))

        self.tablo.cellClicked.connect(self.secildi)

    def secildi(self, row, col):
        ad = self.tablo.item(row, 0).text()
        katsayi = float(self.tablo.item(row, 1).text())

        QMessageBox.information(self, "Seçildi", f"Ad: {ad}\nKatsayı: {katsayi}")

if __name__ == "__main__":
    app = QApplication([])
    p = Pencere()
    p.show()
    app.exec()
