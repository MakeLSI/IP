#------------------------------------------------------------------------------
#
# ML1-VIA-ML2 Pcell for Hibikino
#
# Note: The first argument is always the cellView of the subMaster.
#       All subsequent arguments should have default values and will
#       be passed by name. Each argument should be seperated by a comma
#	and whitespace.
#
#------------------------------------------------------------------------------

# Import the db wrappers
from ui import *

# The entry point. The function name *must* match the filename.
def ml1via_master(cv, nx=1, ny=1) :
	lib = cv.lib()
	dbu = lib.dbuPerUU()

	# Some predefined rules
        VIA_width = int(4 * dbu)
        VIA_space = int(4 * dbu)
        ML1_ovlp_VIA = int(2 * dbu)
        ML2_ovlp_VIA = int(2 * dbu)
        
	tech = lib.tech()

	ML1 = tech.getLayerNum("ML1", "drawing")
	VIA = tech.getLayerNum("VIA", "drawing")
	ML2 = tech.getLayerNum("ML2", "drawing")
        sx = VIA_width * nx + VIA_space * (nx-1) + 2 * ML1_ovlp_VIA;
        sy = VIA_width * ny + VIA_space * (ny-1) + 2 * ML1_ovlp_VIA;
        x0 = -(VIA_width * (nx-1) + VIA_space * (nx-1))/2
        y0 = -(VIA_width * (ny-1) + VIA_space * (ny-1))/2
        r = Rect(-sx/2, -sy/2, sx/2, sy/2)
        ml1 = cv.dbCreateRect(r, ML1)
        ml2 = cv.dbCreateRect(r, ML2)
        print sx, sy, x0, y0
	for x in range(nx) :
                for y in range(ny) :
                        r = Rect(x0 + (VIA_space + VIA_width) * x - VIA_width/2,
                                 y0 + (VIA_space + VIA_width) * y - VIA_width/2,
                                 x0 + (VIA_space + VIA_width) * x + VIA_width/2,
                                 y0 + (VIA_space + VIA_width) * y + VIA_width/2)
                        via = cv.dbCreateRect(r, VIA)
#	# Device type
#	cv.dbAddProp("use", "mos")

	# Update the bounding box
	cv.update()
