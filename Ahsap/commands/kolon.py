from PySide2 import QtWidgets, QtCore, QtUiTools
import FreeCAD as App
import FreeCADGui as Gui
from .Class.Geom import Geo

class KesitPencere(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(KesitPencere, self).__init__(parent)
        # Pencere boyutunu sabitle
        self.setFixedSize(300, 300)  # genişlik=400, yükseklik=300

        # --- UI dosyasını yükle ---
        loader = QtUiTools.QUiLoader()

        ui_file = QtCore.QFile(r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit.ui")
        if not ui_file.open(QtCore.QFile.ReadOnly):
            raise RuntimeError("UI dosyası açılamadı!")

        # UI'yı yükle
        self.ui = loader.load(ui_file)
        ui_file.close()

        # --- UI’yı ana pencerenin içine ekle ---
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

        #Butonlar
        self.ui.pushButton_ucgen.clicked.connect(self.kesit_ucgen)
        self.ui.pushButton_dikdortgen.clicked.connect(self.kesit_dikdortgen)
        self.ui.pushButton_daire.clicked.connect(self.kesit_daire)
    
    def kesit_ucgen(self):
        pass
    
    def kesit_dikdortgen(self):
        # Yeni pencereyi oluştur
        self.yeni_pencere = MetrikPencere(kesit="dikdortgen")
        self.yeni_pencere.show()

        # Mevcut pencereyi kapat
        self.close()
    
    def kesit_daire(self):

        # Yeni pencereyi oluştur
        self.yeni_pencere = MetrikPencere(kesit="daire")
        self.yeni_pencere.show()

        # Mevcut pencereyi kapat
        self.close()

        




class MetrikPencere(QtWidgets.QWidget):
    def __init__(self,kesit:str):
        self.kesit = kesit
        super().__init__()
        self.setFixedSize(300, 300)  # istersen boyutu sabitle

        if kesit == "ucgen":

            # --- UI dosyasını yükle ---
            loader = QtUiTools.QUiLoader()
            ui_file = QtCore.QFile(r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit_dikdortgen.ui")
            if not ui_file.open(QtCore.QFile.ReadOnly):
                raise RuntimeError("UI dosyası açılamadı!")

            self.ui = loader.load(ui_file)
            ui_file.close()

        elif kesit == "dikdortgen":

            # --- UI dosyasını yükle ---
            loader = QtUiTools.QUiLoader()
            ui_file = QtCore.QFile(r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit_dikdortgen.ui")
            if not ui_file.open(QtCore.QFile.ReadOnly):
                raise RuntimeError("UI dosyası açılamadı!")

            self.ui = loader.load(ui_file)
            ui_file.close()

        if kesit == "daire":

            # --- UI dosyasını yükle ---
            loader = QtUiTools.QUiLoader()
            ui_file = QtCore.QFile(r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit_daire.ui")
            if not ui_file.open(QtCore.QFile.ReadOnly):
                raise RuntimeError("UI dosyası açılamadı!")

            self.ui = loader.load(ui_file)
            ui_file.close()

        # --- UI’yı pencereye ekle ---
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)


        self.ui.pushButton_ekle.clicked.connect(self.ekle)

    
    def ekle(self): 
        doc = App.ActiveDocument
        sel = Gui.Selection.getSelectionEx()

        if sel:
            obj = sel[0]                 # seçilen ana obje (Sketch)
            sub = obj.SubObjects[0]      # seçilen alt obje (Vertex)

            try:
               if(self.kesit == "dikdortgen"):
                    p = sub.Point            # global koordinat

                    # --- Kutu Oluştur ---
                    box = doc.addObject("Part::Box", "Kutu")

                    L = self.ui.spinBox_l.value()
                    W = self.ui.spinBox_h.value()
                    H = self.ui.spinBox_b.value()

                    box.Length = H
                    box.Width  = W
                    box.Height = L

                    box.Placement.Base = App.Vector(
                        p.x - H/2,
                        p.y - W/2,
                        p.z - 0 #zeminde olacağı için
                    )

                    doc.recompute()
                    App.Console.PrintMessage("Kutu çizildi.\n")

                    self.close()



            except:
                App.Console.PrintMessage("Vertex seçilmedi!")
        else:
            App.Console.PrintMessage("Hiçbir şey seçilmedi!")

# Komut sınıfı
class Kolon:
    def Activated(self):
        global pencere
        pencere = KesitPencere()
        pencere.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        pencere.show()
        pencere.raise_()  # Öne getir

    def GetResources(self):
        return {
            "MenuText": "Kolon",
            "ToolTip": "Yeni bir Kolon oluşturur",
            "Pixmap": ""
        }

Gui.addCommand("Kolon", Kolon())
