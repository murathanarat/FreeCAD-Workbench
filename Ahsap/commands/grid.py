import FreeCADGui as Gui
import FreeCAD  as App
from PySide2 import QtWidgets,QtCore,QtUiTools

#Test için boş pencere
class pencere(QtWidgets.QDialog):
    def __init__(self, parent=Gui.getMainWindow()):
        super(pencere, self).__init__(parent)

        self.setWindowTitle("Penceresi")
        self.setFixedSize(300, 300)



# Kesit özelikleri için panel
class KesitPanel:
    def __init__(self):
        #.ui dosyamızı eklemek için
        loader = QtUiTools.QUiLoader()

        #.ui dosyamızın yolu ********burası değiştirilecek *******
        ui_file = QtCore.QFile(r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.form = loader.load(ui_file)
        ui_file.close()


        # sinyal bağlama
        self.form.pushButton_daire.clicked.connect(self.daireTiklandi)
        self.form.pushButton_dikdortgen.clicked.connect(self.dikdortgenTiklandi)
        self.form.pushButton_ucgen.clicked.connect(self.ucgenTiklandi)

    #Başlarken gereken butonlar tamam ve iptal sadece iptali aldık
    def getStandardButtons(self):
        return int(
            #dalog panelinden aldık
            QtWidgets.QDialogButtonBox.Cancel
        )

    #Tamam tuşunu eklemediğimiz için bursaının bir önemi yok 
    #*****sil*****
    def accept(self):
        """global pencere
        pencere = pencere()
        pencere.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        pencere.show()
        pencere.raise_()  # Öne getir"""
        
    #İptal tuşuna diyalog panelini kapamayı atadık
    def reject(self):
        Gui.Control.closeDialog()

    #Daire tuşuna basılırsa kesit alanımız için gereken .ui dosyası gelecek
    def daireTiklandi(self):
        #Kesit alan bilgisi
        self.kesit = "daire"
        #Panel oluşturuldu
        form = self.MetrikPanel(self)
        #önceki panel silindi
        Gui.Control.closeDialog()
        #Yeni dialog paneli eklendi
        Gui.Control.showDialog(form)
        
    def dikdortgenTiklandi(self):
        self.kesit = "dikdortgen"
        form = self.MetrikPanel(self)
        Gui.Control.closeDialog()
        Gui.Control.showDialog(form)
        
    def ucgenTiklandi(self):
        self.kesit = "ucgen"
        form = self.MetrikPanel(self)
        Gui.Control.closeDialog()
        Gui.Control.showDialog(form)
        


    #Metriklerimizi gireceğimiz panel
    class MetrikPanel:
        #Parent kesitpanel
        def __init__(self,parent):
            self.parent = parent
            loader = QtUiTools.QUiLoader()

            # Eğer kesit daire seçilmişse gereken .ui dosyasını yükler
            
            if parent.kesit == "daire":
                ui_path = r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit_daire.ui"
            if parent.kesit == "dikdortgen":
                ui_path = r"C:\Users\murat\Desktop\FreeCAD 1.0\Mod\Ahsap\Ui\kesit_dikdortgen.ui"
            if parent.kesit == "ucgen":
                pass

            if parent.kesit == None:
                return 0
            
            ui_file = QtCore.QFile(ui_path)
            ui_file.open(QtCore.QFile.ReadOnly)
            self.form = loader.load(ui_file)
            ui_file.close()

        def getStandardButtons(self):
            return int(
                QtWidgets.QDialogButtonBox.Ok |
                QtWidgets.QDialogButtonBox.Cancel
            )
        
        def accept(self):
            self.ekle()
            Gui.Control.closeDialog()

        def reject(self):
            Gui.Control.closeDialog()

        def ekle(self): 
            doc = App.ActiveDocument
            sel = Gui.Selection.getSelectionEx()

            if sel:
                obj = sel[0]                 # seçilen ana obje (Sketch)
                sub = obj.SubObjects[0]      # seçilen alt obje (Vertex)

                try:
                    if(self.parent.kesit == "dikdortgen"):
                        p = sub.Point            # global koordinat
                        # --- Kutu Oluştur ---
                        box = doc.addObject("Part::Box", "Kutu")
                        L = self.form.spinBox_l.value()
                        W = self.form.spinBox_h.value()
                        H = self.form.spinBox_b.value()
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
class Grid:
    def Activated(self):
        """global pencere
        pencere = Pencere()
        pencere.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        pencere.show()
        pencere.raise_()  # Öne getir"""
        Gui.Control.showDialog(KesitPanel())


        

    def GetResources(self):
        return {
            "MenuText": "Grid",
            "ToolTip": "Grid",
            "Pixmap": ""
        }
    


Gui.addCommand("Grid", Grid())