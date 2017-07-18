# 2um Hibikino DRC
# ver1.00 : 2017/1/24: akita11 akita@ifdl.jp
# ver1.10 : 2017/7/15: akita11 : VIA-Poly/CNA overlap, NWL-PWL/NSL-PSL overlap

# simpe function to print # errors - unused.
def printErrors(msg) :
	n = geomGetCount()
	if n > 0 :
		print n, msg

# Initialise DRC package. 
from ui import *
cv = ui().getEditCellView()
geomBegin(cv)

# Get raw layers
NWL = geomGetShapes("NWL", "drawing")
PWL = geomGetShapes("PWL", "drawing")
CST = geomGetShapes("CST", "drawing")
ACT = geomGetShapes("ACT", "drawing")
VTN = geomGetShapes("VTN", "drawing")
VTP = geomGetShapes("VTP", "drawing")
POL = geomGetShapes("POL", "drawing")
NSL = geomGetShapes("NSL", "drawing")
PSL = geomGetShapes("PSL", "drawing")
CNA = geomGetShapes("CNA", "drawing")
CNP = geomGetShapes("CNP", "drawing")
ML1 = geomGetShapes("ML1", "drawing")
VIA = geomGetShapes("VIA", "drawing")
ML2 = geomGetShapes("ML2", "drawing")

# Form derived layers
CDN = geomAnd(NSL, ACT);
CDP = geomAnd(PSL, ACT);
NMOS = geomAnd(CDN, POL);
PMOS = geomAnd(CDP, POL);

# Form connectivity
geomConnect( [
        [CNA, CDN, ML1],
        [CNA, CDP, ML1],
        [CNP, POL, ML1],
        [VIA, ML1, ML2],
	     ] )

print "Check GAP"
geomSpace(ACT, 4, "ACT space < 4")
geomSpace(POL, 2, "POL space < 2")
geomSpace(ML1, 4, "ML1 space < 4")
geomSpace(ML2, 4, "ML2 space < 4")
geomSpace(CNA, 2, "CNA space < 2")
geomSpace(CNP, 2, "CNP space < 2")
geomSpace(VIA, 4, "VIA space < 4")
geomSpace(POL, 2, "POL space < 2")
geomSpace(POL, 2, "POL space < 2")
geomSpace(NWL, 4, "NWL space < 4")
geomSpace(PWL, 4, "PWL space < 4")
geomSpace(CST, 4, "CST space < 4")

geomSpace(NSL, 2, "NSL space < 2") # add 170715 by akita11
geomSpace(PSL, 2, "PSL space < 2") # add 170715 by akita11
geomSpace(VTN, 2, "VTN space < 2") # add 170715 by akita11
geomSpace(VTP, 2, "VTP space < 2") # add 170715 by akita11

#geomSpace(VIA, POL, 0, "VIA/POL < 1")
#geomSpace(VIA, CNA, 1, "VIA/CND&CDP < 1")

print "Check Width"
geomWidth(ACT, 4, "ACT width < 4")
geomWidth(NWL, 6, "NWL width < 6")
geomWidth(PWL, 6, "PWL width < 6")
geomWidth(CST, 4, "CST width < 4")
geomWidth(NSL, 8, "NSL width < 8")
geomWidth(PSL, 8, "PSL width < 8")
geomWidth(POL, 2, "POL width < 2")
geomWidth(ML1, 6, "ML1 width < 6")
geomWidth(ML2, 6, "ML2 width < 6")
geomWidth(VIA, 4, "VIA width < 4")
geomWidth(CNA, 2, "CNA width < 2")
geomWidth(CNP, 2, "CNP width < 2")

print "Check Enclose"
CDA = geomOr(CDN, CDP) # both active
AWL = geomOr(NWL, PWL) # both well
geomEnclose(ML1, CNA, 2, "ML1/CNA < 2")
geomEnclose(CDA, CNA, 2, "CDN&CDP/CNA < 2")
geomEnclose(ML1, CNP, 2, "ML1/CNP < 2")
geomEnclose(POL, CNP, 2, "POL/CNP < 2")
geomEnclose(VIA, ML1, 2, "ML1/VIA < 2")
geomEnclose(VIA, ML2, 2, "ML1/VIA < 2")
geomEnclose(NSL, CDN, 2, "NSL/ACT < 2")
geomEnclose(PSL, CDP, 2, "NSL/ACT < 2")
geomEnclose(CST, CDA, 3, "CDN&CDP/CST < 3")
geomEnclose(AWL, CST, 2, "CST/NWL&PWL < 2")

print "Check VIA/Contact size"
geomArea(CNA, 4, 4, "CNA size != 2x2")
geomArea(CNP, 4, 4, "CNP size != 2x2")
geomArea(VIA, 16, 16, "VIA size != 4x4")

print "Check MOS gate extension"
geomExtension(POL, ACT, 2, "POL gate extension < 2")

print "Check Overlap"
#geomOverlap(NWL, PWL, 0, "NWL/PWL overlap")
NWLPWL = geomAnd(NWL, PWL)
geomArea(NWLPWL, 0, 0, "NWL-PWL overlap")

#geomOverlap(NSL, PSL, 0, "NSL/PSL overlap")
NSLPSL = geomAnd(NSL, PSL)
geomArea(NSLPSL, 0, 0, "NSL-PSL overlap")

#geomSpace(VIA, POL, 0, "VIA/POL < 1")
POLVIA = geomAnd(POL, VIA)
geomArea(POLVIA, 0, 0, "Poly-VIA overlap")

#geomSpace(VIA, CNA, 1, "VIA/CND&CDP < 1")
CNAVIA = geomAnd(VIA, CNA)
geomArea(CNAVIA, 0, 0, "CNA-VIA overlap")

print "Check stand-alone Active"
ASL = geomOr(NSL, PSL) # both select
NASL = geomNot(ASL)
AACT = geomAnd(ACT, NASL)
geomArea(AACT, 0, 0, "ACT without NSL/PSL")

# Exit DRC package, freeing memory
geomEnd()
#ui().winFit()
