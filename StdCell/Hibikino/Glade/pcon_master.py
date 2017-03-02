#------------------------------------------------------------------------------
#
# Pact-CNA-ML1 Pcell for Hibikino
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
def pcon_master(cv, nx=1, ny=1) :
	lib = cv.lib()
	dbu = lib.dbuPerUU()

	# Some predefined rules
	CNT_width = int(2 * dbu) # CNT wize
	CNT_space = int(2 * dbu) # CNT space
	PWL_ovlp_ACT = int(10 * dbu) # ACT-PWL overlap
        CST_ovlp_ACT = int(8 * dbu) # ACT-CST overlap
        NSL_ovlp_ACT = int(2 * dbu) # ACT-NSL overlap
	POL_ovlp_CNT = int(2 * dbu) # CNP-POL overlap
	ACT_ovlp_CNT = int(2 * dbu) # CNA-ACT overlap
	ML1_ovlp_CNT = int(2 * dbu) # CNA&CNP-ML1 overlap
        POL_POL_space = int(3 * dbu) # POL-POL space
        POL_CNT_space = int(4 * dbu) # POL-CNT space
	tech = lib.tech()

        # Create gate / poly fingers
	ACT = tech.getLayerNum("ACT", "drawing")
	PSL = tech.getLayerNum("PSL", "drawing")
        CNA = tech.getLayerNum("CNA", "drawing")
        ML1 = tech.getLayerNum("ML1", "drawing")
        sx = CNT_width * nx + CNT_space * (nx-1) + 2 * POL_ovlp_CNT;
        sy = CNT_width * ny + CNT_space * (ny-1) + 2 * POL_ovlp_CNT;
        x0 = -(CNT_width * (nx-1) + CNT_space * (nx-1))/2
        y0 = -(CNT_width * (ny-1) + CNT_space * (ny-1))/2
        r = Rect(-sx/2, -sy/2, sx/2, sy/2)
        act = cv.dbCreateRect(r, ACT)
        ml1 = cv.dbCreateRect(r, ML1)
        r = Rect(-sx/2-NSL_ovlp_ACT, -sy/2-NSL_ovlp_ACT, sx/2+NSL_ovlp_ACT, sy/2+NSL_ovlp_ACT)
        psl = cv.dbCreateRect(r, PSL)
        print sx, sy, x0, y0
	for x in range(nx) :
                for y in range(ny) :
                        r = Rect(x0 + (CNT_space + CNT_width) * x - CNT_width/2,
                                 y0 + (CNT_space + CNT_width) * y - CNT_width/2,
                                 x0 + (CNT_space + CNT_width) * x + CNT_width/2,
                                 y0 + (CNT_space + CNT_width) * y + CNT_width/2)
                        cnp = cv.dbCreateRect(r, CNA)
#	# Device type
#	cv.dbAddProp("use", "mos")

	# Update the bounding box
	cv.update()
