from Class.Geom import Geo
from Class.Tablolar import *
from Class.Kat import *
from Class.Malzeme import Malzeme
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,QHeaderView
import os


class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        # Bu Python dosyasının klasörü
        klasor = os.path.dirname(os.path.abspath(__file__))

        # main.ui tam yolu
        ui_dosyasi = os.path.join(klasor, "main.ui")

        uic.loadUi(ui_dosyasi, self)



        self.Malzeme_tablo(malzemeler_path)
        self.Cn_tablo(tablo1_4)
        self.Cy_tablo(tablo1_6)
        self.tablo_doldur(table_widget=self.omega_tableWidget,dosya_yolu=tablo1_3)

        

        self.hesapla_pushButton.clicked.connect(self.hesapla)
    
    def tablo_doldur(self, table_widget, dosya_yolu):


        # Dosyayı oku
        df = pd.read_csv(dosya_yolu, sep=';')

        # Sütun ve satır sayısı
        table_widget.setColumnCount(df.columns.size)
        table_widget.setRowCount(len(df))
        table_widget.setHorizontalHeaderLabels(list(df.columns))

        # Verileri tabloya ekle
        for i, row in enumerate(df.itertuples()):
            for j, value in enumerate(row[1:]):  # row[0] index olduğu için 1'den başlıyoruz
                table_widget.setItem(i, j, QTableWidgetItem(str(value)))

        # Sütun genişliklerini ayarla
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)    
    
    def Cn_tablo(self, dosya_yolu):
        # Txt dosyasını pandas ile oku
        Cn_df = pd.read_csv(dosya_yolu, sep=';')

        # Sütun ve satır sayısını ayarla
        self.Cn_tableWidget.setColumnCount(Cn_df.columns.size)
        self.Cn_tableWidget.setRowCount(len(Cn_df))
        self.Cn_tableWidget.setHorizontalHeaderLabels(list(Cn_df.columns))

        # Verileri tabloya ekle
        for i, row in enumerate(Cn_df.itertuples()):
            for j, value in enumerate(row[1:]):  # row[0] index olduğu için 1'den başlıyoruz
                self.Cn_tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        # Sütun genişliklerini içerik ve başlığa göre ayarla
        self.Cn_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    
    def Cy_tablo(self, dosya_yolu):
        # Txt dosyasını pandas ile oku
        Cy_df = pd.read_csv(dosya_yolu, sep=';')

        # Sütun ve satır sayısını ayarla
        self.Cy_tableWidget.setColumnCount(Cy_df.columns.size)
        self.Cy_tableWidget.setRowCount(len(Cy_df))
        self.Cy_tableWidget.setHorizontalHeaderLabels(list(Cy_df.columns))

        # Verileri tabloya ekle
        for i, row in enumerate(Cy_df.itertuples()):
            for j, value in enumerate(row[1:]):  # row[0] index olduğu için 1'den başlıyoruz
                self.Cy_tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        # Sütun genişliklerini içerik ve başlığa göre ayarla
        self.Cy_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def Malzeme_tablo(self,dosya_yolu):
        malzeme_ad = pd.read_csv(dosya_yolu, sep=';')


        # Sütun ve satır sayısını ayarla
        self.Malzeme_tableWidget.setColumnCount(malzeme_ad.columns.size)
        self.Malzeme_tableWidget.setRowCount(len(malzeme_ad))
        self.Malzeme_tableWidget.setHorizontalHeaderLabels(list(malzeme_ad.columns))

        # Verileri tabloya ekle
        for i, row in enumerate(malzeme_ad.itertuples()):
            for j, value in enumerate(row[1:]):  # row[0] index olduğu için 1'den başlıyoruz
                self.Malzeme_tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        # Sütun genişliklerini içerik ve başlığa göre ayarla
        self.Malzeme_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def hesapla(self):
        # LineEdit değerlerini al
        try:
            b = float(self.b_lineEdit.text())
        except ValueError:
            b = 140
        try:
            h = float(self.h_lineEdit.text())
        except ValueError:
            h = 140
        try:
            L = float(self.l_lineEdit.text())
        except ValueError:
            L = 3000
        try:
            g = float(self.g_lineEdit.text())
        except ValueError:
            g = 5
        try:
            q = float(self.q_lineEdit.text())
        except ValueError:
            q = 2
        try:
            E = float(self.e_lineEdit.text())
        except ValueError:
            E = 11000

        malzeme_ad = self.malzeme_ad_sec()
        malzeme = Malzeme(malzeme_adi=malzeme_ad)

        nem_durumu = self.C_n_sec()
        cn = C_n(nem_durumu=nem_durumu)



        
     

        # Hesaplama (örnek)
        Ag = b * h
        print(f"b={b}, h={h}, L={L}, g={g}, q={q}, E={E}")
        print(malzeme)
        print(f"Kesit alanı Ag={Ag} mm²")
        print(cn)

    def malzeme_ad_sec(self):
        selected_rows = self.Malzeme_tableWidget.selectionModel().selectedRows()
        if selected_rows:
            row_index = selected_rows[0].row()
            value = self.Malzeme_tableWidget.item(row_index, 0).text()
            return value
        
    def C_n_sec(self):
        selected_rows = self.Cn_tableWidget.selectionModel().selectedRows()
        if selected_rows:
            row_index = selected_rows[0].row()
            value = self.Cn_tableWidget.item(row_index, 0).text()
            print
            return value

if __name__ == "__main__":
    app = QApplication([])
    pencere = AnaPencere()
    pencere.show()
    app.exec()


b = 140
h = 140
L = 3000
malzeme = Malzeme("C24")

cb = 0
omega_ = omega()
cn = C_n("Az")

cy_tablo = C_y_tablo("Masif Ahşap","Az")

cy = C_y(kuvvet(),C_y_tablo=cy_tablo)



print(malzeme)
Ag = A_g(b,h)
lx = ly = l(b,h)
iy = i(l=lx,Ag=Ag)
lambda_y = lambda_xy(l=L,i=iy)
fEy = f_E_xy(malzeme.get("E005"),lambda_xy=lambda_y)
"""fc0d = f_c_0_d(f_c_0_k=malzeme.get("fc0k"),C_n=cn,C_y=cy,C_b=cb,omega=)"""
