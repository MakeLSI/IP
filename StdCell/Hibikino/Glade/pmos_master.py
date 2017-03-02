#------------------------------------------------------------------------------
#
# NMOS Pcell for Hibikino
#	Create a Pcell with parameters w (width of gate),
#	l (length of gate), m (number of gates).
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
def pmos_master(cv, w=18, l=2, m=1, poly_con=0) :
	lib = cv.lib()
	dbu = lib.dbuPerUU()
	width = int(w * dbu) # gate width
	length = int(l * dbu) # gate length
	fingers = int(m)

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
        GATE_ext = int(3 * dbu) # gate extension
	tech = lib.tech()

        # Create gate / poly fingers
	POL = tech.getLayerNum("POL", "drawing")
        CNP = tech.getLayerNum("CNP", "drawing")
        ML1 = tech.getLayerNum("ML1", "drawing")
	width_gate = width + 2 * GATE_ext
	for i in range(fingers) :
                ii = i * 2
                gate_xi = (CNT_width + 2 * POL_CNT_space + length) * (ii - (fingers - 1))/2
	        r = Rect(gate_xi - length/2, -width_gate/2, gate_xi + length/2, width_gate/2)
	        gate = cv.dbCreateRect(r, POL)
                if poly_con :
                        r = Rect(gate_xi - (CNT_width + 2 * POL_ovlp_CNT)/2,
                                 width_gate/2,
                                 gate_xi + (CNT_width + 2 * POL_ovlp_CNT)/2,
                                 width_gate/2 + CNT_width + 2 * POL_ovlp_CNT)
                        gatecon = cv.dbCreateRect(r, POL)
                        r = Rect(gate_xi - (CNT_width + 2 * ML1_ovlp_CNT)/2,
                                 width_gate/2,
                                 gate_xi + (CNT_width + 2 * ML1_ovlp_CNT)/2,
                                 width_gate/2 + CNT_width + 2 * POL_ovlp_CNT)
                        gateml1 = cv.dbCreateRect(r, ML1)
                        r = Rect(gate_xi - CNT_width/2,
                                 width_gate/2 + POL_ovlp_CNT,
                                 gate_xi + CNT_width/2,
                                 width_gate/2 + POL_ovlp_CNT + CNT_width)
                        gatecnp = cv.dbCreateRect(r, CNP)
                
	# Create S/D contacts
	CNA = tech.getLayerNum("CNA", "drawing")
        N_CNT = int((width + CNT_space - 2 * ACT_ovlp_CNT) / (CNT_width + CNT_space))
        for i in range(fingers + 1) :
                ii = i * 2
                cnt_xi = (CNT_width + 2 * POL_CNT_space + length) * (ii - fingers)/2
                for j in range(N_CNT) :
                        jj = j * 2
                        cnt_yj = (CNT_width + CNT_space) * (jj - (N_CNT - 1))/2
                        print j, N_CNT,cnt_yj
                        r = Rect(cnt_xi - CNT_space/2, cnt_yj - CNT_space/2, cnt_xi + CNT_space/2, cnt_yj + CNT_space/2)
                        cnt_a = cv.dbCreateRect(r, CNA)


        # Create active
	ACT = tech.getLayerNum("ACT", "drawing")
	length_act = (CNT_width + 2 * POL_CNT_space + length) * (fingers - 1) + 2 * (CNT_width + POL_CNT_space + ACT_ovlp_CNT) + length
	r = Rect(-length_act/2, -width/2, length_act/2, width/2)
	active = cv.dbCreateRect(r, ACT)

        # Create NSL
	NSL = tech.getLayerNum("PSL", "drawing")
	length_nsl = length_act + NSL_ovlp_ACT * 2
        width_nsl = width + NSL_ovlp_ACT * 2
	r = Rect(-length_nsl/2, -width_nsl/2, length_nsl/2, width_nsl/2)
	nsl = cv.dbCreateRect(r, NSL)

	# Create ML1
        length_ml1 = CNT_width + 2 * ML1_ovlp_CNT
        for i in range(fingers + 1) :
                ii = i * 2
                ml1_xi = (CNT_width + 2 * POL_CNT_space + length) * (ii - fingers)/2

                r = Rect(ml1_xi - length_ml1/2, -width/2, ml1_xi + length_ml1/2, width/2)
                ml1 = cv.dbCreateRect(r, ML1)

        # Create CST
	CST = tech.getLayerNum("CST", "drawing")
	length_cst = length_act + CST_ovlp_ACT * 2
        width_cst = width + CST_ovlp_ACT * 2
	r = Rect(-length_cst/2, -width_cst/2, length_cst/2, width_cst/2)
	cst = cv.dbCreateRect(r, CST)

        # Create PWL
	PWL = tech.getLayerNum("NWL", "drawing")
	length_pwl = length_act + PWL_ovlp_ACT * 2
        width_pwl = width + PWL_ovlp_ACT * 2
	r = Rect(-length_pwl/2, -width_pwl/2, length_pwl/2, width_pwl/2)
	pwl = cv.dbCreateRect(r, PWL)

	# Device type
	cv.dbAddProp("use", "mos")

	# Update the bounding box
	cv.update()
