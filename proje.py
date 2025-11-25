import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class NemPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nem Durumu Tablosu")
        layout = QVBoxLayout(self)

        # txt dosyasını pandas ile oku
        df = pd.read_csv(r"C:\Users\murat\Desktop\calıs\Git\Proje\Tablolar\tablo1.4.txt", sep=';', index_col=0)

        # QTableWidget oluştur
        self.tablo = QTableWidget()
        self.tablo.setColumnCount(df.columns.size)
        self.tablo.setRowCount(len(df))
        self.tablo.setHorizontalHeaderLabels(list(df.columns))
        layout.addWidget(self.tablo)

        # Verileri tabloya ekle
        for i, row in enumerate(df.itertuples()):
            for j, value in enumerate(row[1:]):  # row[0] index olduğu için 1'den başlıyoruz
                self.tablo.setItem(i, j, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication([])
    pencere = NemPencere()
    pencere.show()
    app.exec()
