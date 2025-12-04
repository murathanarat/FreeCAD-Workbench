from Class.Geom import Geo
from Class.Tablolar import *
from Class.Kat import *
from Class.Malzeme import Malzeme
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,QHeaderView,QFileDialog
import os
import yaz
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPalette, QColor



class AnaPencere(QMainWindow):
    def style(self):
    # Tab widget ve tab sayfaları için QSS
        self.setStyleSheet("""
            /* Ana pencere */
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }

            /* Etiketler */
            QLabel {
                color: #ffffff;
            }

            /* Butonlar */
            QPushButton {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #505357;
            }

            /* Menü çubuğu */
            QMenuBar {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QMenuBar::item:selected {
                background-color: #505357;
            }

            /* Status bar */
            QStatusBar {
                background-color: #2b2b2b;
                color: #ffffff;
            }

            /* Giriş alanları */
            QLineEdit, QTextEdit, QPlainTextEdit, QComboBox, QSpinBox, QDoubleSpinBox {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #555555;
            }

            /* Scroll bar */
            QScrollBar:vertical, QScrollBar:horizontal {
                background: #2b2b2b;
                width: 12px;
                margin: 0px;
            }
            QScrollBar::handle {
                background: #505357;
                border-radius: 6px;
            }
            QScrollBar::handle:hover {
                background: #686b6e;
            }
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
            }

            /* CheckBox ve RadioButton */
            QCheckBox, QRadioButton {
                color: #ffffff;
            }

            /* Tab widget */
            QTabWidget::pane {
                border: 1px solid #555555;
                background: #2b2b2b;
            }
            QTabBar::tab {
                background: #3c3f41;
                color: #ffffff;
                padding: 5px;
                border: 1px solid #555555;
            }
            QTabBar::tab:selected {
                background: #505357;
            }

            /* TableWidget */
            QTableWidget {
                background-color: #3c3f41;
                color: #ffffff;
                gridline-color: #555555;
                selection-background-color: #505357;
                selection-color: #ffffff;
            }

            QHeaderView::section {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #555555;
            }

            /* Seçili hücreler */
            QTableWidget::item:selected {
                background-color: #505357;
                color: #ffffff;
            }

            /* Köşe düğmesi (corner button) */
            QTableCornerButton::section {
                background-color: #3c3f41;
                border: 1px solid #555555;
            }

        """)

        
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

        self.Malzeme_tableWidget.cellClicked.connect(self.malzeme_ad_sec)
        self.hesapla_pushButton.clicked.connect(self.hesapla)
        self.actiondocx.triggered.connect(self.yaz_docx)
    
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
            self.b = float(self.b_lineEdit.text())
        except ValueError:
            self.b = 0
        try:
            self.h = float(self.h_lineEdit.text())
        except ValueError:
            self.h = 0
        try:
            self.L = float(self.l_lineEdit.text())
        except ValueError:
            self.L = 0
        try:
            self.G = float(self.g_lineEdit.text())
        except ValueError:
            self.G = 0
        try:
            self.Q = float(self.q_lineEdit.text())
        except ValueError:
            self.Q = 0
        try:
            self.E = float(self.e_lineEdit.text())
        except ValueError:
            self.E = 0

        try:

            self.kuvvet = kuvvet(
                    G=self.G,
                    Q=self.Q,
                    E=self.E,
                )
            self.nem_durumu = self.C_n_sec()
            self.C_n = C_n(nem_durumu=self.nem_durumu)
            #self.C_y = C_y(kuvvet= self.kuvvet)

            #self.C_b = C_b(h=self.h,malzeme="Masif Ahşap")
        except:
            QMessageBox.warning(self, "Uyarı", "Tablo Seçimlerini yapınız")
        
        self.A_g = A_g(b=self.b,h=self.h)
        self.l_ = l(b=self.b,h=self.h)
        self.i_ = i(l=self.l_,A_g=self.A_g)
        self.lambda_ = lambda_xy(l=self.l_,i=self.i_)
        self.f_E_y = f_E_xy(E005=self.malzeme.get("E005"),lambda_xy=self.lambda_)

        #Düzenle
        #self.f_c_0_d = f_c_0_d(f_c_0_k=self.malzeme.get("fc0d"),C_n=self.C_n,C_y=self.C_y,C_b=self.C_b)
        self.f_c_0_d = 0
        
        self.C_p = C_p(
            f_E=f_E_xy(E005=self.malzeme.get("E005"),lambda_xy=self.lambda_),
            f_c_0_k=self.malzeme.get("fc0k")
            )
        self.sigma_c_0_d = sigma_c_0_d()
        


        

        # Hesaplama (örnek)
        self.Ag = self.b * self.h
        
    """
    Burada docx dosyası oluturuluyor
    """
    def yaz_docx(self):

        dosya_yolu, _ = QFileDialog.getSaveFileName(
            self, 
            "DOCX Kaydet", 
            "", 
            "Word Dosyaları (*.docx)"
        )

        if dosya_yolu:
            # Eğer kullanıcı uzantı eklemediyse otomatik ekle
            if not dosya_yolu.endswith(".docx"):
                dosya_yolu += ".docx"

            try:
                # Word dosyasını oluştur
                print(dosya_yolu)
                #Docx dosyası oluşturma
                yaz.kolonun_kayipsiz_kesit_alani(
                    path=dosya_yolu,
                    b=self.b,
                    h=self.h,
                    L=self.L,
                    l_=self.l_,
                    i_=self.i_,
                    lambda_= self.lambda_,
                    f_E_y=self.f_E_y,
                    f_c_0_d=self.f_c_0_d,
                    C_p=self.C_p,
                    sigma_c_0_d=self.sigma_c_0_d
                )

                QMessageBox.information(self, "Başarılı", f"DOSYA KAYDEDİLDİ:\n{dosya_yolu}")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Bir hata oluştu:\n{str(e)}")
        else:
            QMessageBox.warning(self, "İptal", "Dosya kaydetme işlemi iptal edildi.")
        

    def malzeme_ad_sec(self):
        selected_rows = self.Malzeme_tableWidget.selectionModel().selectedRows()
        if selected_rows:
            row_index = selected_rows[0].row()
            value = self.Malzeme_tableWidget.item(row_index, 0).text()
        self.malzeme_ad = value
        self.malzeme = Malzeme(malzeme_adi=self.malzeme_ad)
        self.textEdit.setPlainText(str(self.malzeme))
        
    def C_n_sec(self):
        selected_rows = self.Cn_tableWidget.selectionModel().selectedRows()
        if selected_rows:
            row_index = selected_rows[0].row()
            value = self.Cn_tableWidget.item(row_index, 0).text()
            return value

if __name__ == "__main__":
    app = QApplication([])
    pencere = AnaPencere()
    pencere.show()
    app.exec()

