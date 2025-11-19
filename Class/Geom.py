from sectionproperties.pre.library.primitive_sections import *
from sectionproperties.analysis.section import Section

class Geo:
    #r:çap
    class Daire:
        def __init__(self,r:float,l:float,l_x:float|None=None,l_y:float|None=None,n:int|None = 32,mesh_size:int|None=500):
            if l_y == None:
                l_y = l
            if l_x == None:
                l_x = l

            self.l_x = l_x     
            self.l_y = l_y     
            self.l = l     

            self.r = r
            self.cir = circular_section(d=r,n=n)
            self.cir.create_mesh(mesh_sizes=mesh_size)
            self.section = Section(geometry=self.cir)
            self.section.calculate_geometric_properties()
            self.kesit_ozelik = self.section.section_props

    class Dortgen:
        def __init__(self,h:float,b:float,l:float,l_x:float|None=None,l_y:float|None=None,mesh_size:int|None=500):
            if l_y == None:
                l_y = l
            if l_x == None:
                l_x = l

            self.l_x = l_x     
            self.l_y = l_y     
            self.l = l
                
            self.h = h
            self.b = b

            self.rec = rectangular_section(d=h,b=b)
            self.rec.create_mesh(mesh_sizes=mesh_size)
            self.section = Section(geometry=self.rec)
            self.section.calculate_geometric_properties()
            self.kesit_ozelik = self.section.section_props

    class Ucgen:
        def __init__(self,h:float,b:float,l:float,l_x:float|None=None,l_y:float|None=None,mesh_size:int|None=500):
            if l_y == None:
                l_y = l
            if l_x == None:
                l_x = l

            self.l_x = l_x     
            self.l_y = l_y     
            self.l = l

            self.h = h
            self.b = b

            self.tri = triangular_section(h=h,b=b)
            self.tri.create_mesh(mesh_sizes=mesh_size)
            self.section = Section(geometry=self.tri)
            self.section.calculate_geometric_properties()
            self.kesit_ozelik = self.section.section_props


