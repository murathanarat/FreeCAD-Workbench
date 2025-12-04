import FreeCADGui as Gui
import FreeCAD as App

class WoodWorkbench (Workbench):

    MenuText = "Wood Struct Workbench"
    ToolTip = "Wood Struct Workbench --------- açıklama"

    # Workbench ilk kez açıldığında çalışır
    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        # Kolon oluşturma vs. fonksiyonları burada import edilecek
        from commands import kolon,grid
        self.list = ["Kolon","Grid"] # a list of command names created in the line above
        self.appendToolbar("My Commands", self.list) # creates a new toolbar with your commands
        self.appendMenu("My New Menu", self.list) # creates a new menu
        self.appendMenu(["An existing Menu", "My submenu"], self.list) # appends a submenu to an existing menu


    # Workbench etkin olduğunda çalışır
    def Activated(self):
        # Aktif edildiğinde döküman oluşur
        # self.document()
        """
        özel kamera ayarı yapmak

        arayüzü güncellemek

        geçici değişkenleri sıfırlamak
        """
        return

    # Workbench kapatıldığında veya başka bir workbench seçildiğinde çağrılır.
    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return


    def ContextMenu(self, recipient):
        """
        recipient:

        view → 3D sahneye sağ tık

        tree → Model ağacına sağ tık

        Bu fonksiyon sağ tık menüsüne komut koymanı sağlar.
        """
        self.appendContextMenu("My commands", self.list)

    def GetClassName(self): 
        # Değiştirme
        return "Gui::PythonWorkbench"
    

    def document(self):
        App.newDocument()
       
Gui.addWorkbench(WoodWorkbench())

"""



    App.setActiveDocument("Unnamed1")
    App.ActiveDocument=App.getDocument("Unnamed1")
    Gui.ActiveDocument=Gui.getDocument("Unnamed1")
    App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch')
    App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.000000, 0.000000, 0.000000, 1.000000))
    App.activeDocument().Sketch.MapMode = "Deactivated"
    Gui.activeDocument().setEdit('Sketch')
    import Show
    ActiveSketch = App.getDocument('Unnamed1').getObject('Sketch')
    tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
    ActiveSketch.ViewObject.TempoVis = tv
    if ActiveSketch.ViewObject.EditingWorkbench:
        tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
    if ActiveSketch.ViewObject.HideDependent:
        tv.hide(tv.get_all_dependent(App.getDocument('Unnamed1').getObject('Sketch'), ''))
    if ActiveSketch.ViewObject.ShowSupport:
        tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
    if ActiveSketch.ViewObject.ShowLinks:
        tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
        tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
        tv.hide(ActiveSketch)
    del(tv)
    del(ActiveSketch)

    ActiveSketch = App.getDocument('Unnamed1').getObject('Sketch')
    if ActiveSketch.ViewObject.RestoreCamera:
        ActiveSketch.ViewObject.TempoVis.saveCamera()
    if ActiveSketch.ViewObject.ForceOrtho:
        ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')"""
