# Hibikino: add VTP/VTN

# Initialise DRC package. 
from ui import *

lib = getLibByName("Hibikino1707") 
cv = lib.dbOpenCellView("00TOP1", "layout", 'a')

# initialise the boolean engine 
geomBegin(cv) 

# set which viewname we want to save to 
setExtViewName("layout") 

# get the layer geometries. 
NWL = geomGetShapes("NWL", "drawing", True) 
PWL = geomGetShapes("PWL", "drawing", True) 
NSL = geomGetShapes("NSL", "drawing", True) 
PSL = geomGetShapes("PSL", "drawing", True) 

# delete VTN/TVP shapes
geomErase("VTN")
geomErase("VTP")

# form intersections 
VN = geomAnd(PWL, NSL)
VP = geomAnd(NWL, PSL)

# save layer back to cellview 
saveDerived(VN, "VTN", "drawing") 
saveDerived(VP, "VTP", "drawing") 

geomEnd()
