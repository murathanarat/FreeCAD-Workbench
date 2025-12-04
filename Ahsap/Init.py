"""FreeCAD init script of Ahsap (Wood Structures) Workbench"""

# ***************************************************************************
# *   Copyright (c) 2025
# *   Mehmet Fatih Arat | Murathan Arat
# *
# *   This file is part of the Ahsap Workbench module for FreeCAD,
# *   designed for creating and analyzing wooden structures.
# *
# *   This program is free software; you can redistribute it and/or modify
# *   it under the terms of the GNU Lesser General Public License (LGPL)
# *   as published by the Free Software Foundation; either version 2 of
# *   the License, or (at your option) any later version.
# *   For details, see the LICENSE text file.
# *
# *   FreeCAD is distributed in the hope that it will be useful,
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# *   GNU Lesser General Public License for more details.
# *
# *   You should have received a copy of the GNU Library General Public
# *   License along with FreeCAD; if not, write to the Free Software
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# *   USA
# *
# ***************************************************************************

# Register import/export types specific to Ahsap Workbench
FreeCAD.addImportType("Ahsap Structural Format (*.ahsap)", "importAhsap")
FreeCAD.addExportType("Ahsap Structural Format (*.ahsap)", "exportAhsap")

print("Ahsap Workbench initialized: Wood structure tools are loaded.")
