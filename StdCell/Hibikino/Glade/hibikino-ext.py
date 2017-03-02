# extraction rule for Hibikino
# ver 1.00 : 2017/1/24: akita11 akita@ifdl.jp

# Initialise boolean package. 
from ui import *
ui = cvar.uiptr
cv = ui.getEditCellView()
geomBegin(cv)
lib = cv.lib()

#print "\n# Loading pcells"
#ui.loadPCell(lib.libName(), "h_nmos_ex")
#ui.loadPCell(lib.libName(), "p_nmos_ex")

print "# Get raw layers"
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

print "# Form derived layers"
#bkgnd     = geomBkgnd()
#psub      = geomAndNot(bkgnd, nwell)

gate      = geomAnd(POL, ACT)
diff      = geomAndNot(ACT, gate)
ndiff     = geomAnd(diff, NSL)
pdiff     = geomAnd(diff, PSL)
ntap      = geomAnd(ndiff, NWL)
ptap      = geomAnd(pdiff, PWL)
ngate     = geomAnd(gate, NSL) # geomAnd(gate, ndiff) -> x
pgate     = geomAnd(gate, PSL) # geomAnd(gate, npiff) -> x

print "# Label nodes"
# This must be done BEFORE geomConnect.
geomLabel(POL, "POL", "drawing")
geomLabel(ML1, "ML1", "drawing")
geomLabel(ML2, "ML2", "drawing")

print "# Form connectivity"
geomConnect( [
              [ptap, pdiff, PWL],
              [ntap, ndiff, NWL],
              [CNA, ndiff, pdiff, ML1],
              [CNP, POL, ML1],
              [VIA, ML1, ML2],
	     ] )

# Save connectivity to extracted view. Saved layers must be
# ones previously connected by geomConnect. Any derived
# layers must be saved to a named layer (e.g. psub below)
print "# Save interconnect"
saveInterconnect([
                PWL,
		NWL,
		[ntap, "ACT"],
		[ptap, "ACT"],
		[ndiff, "ACT"],
		[pdiff, "ACT"],
		[POL, "POL"],
		CNA,
		CNP,
		ML1,
		VIA,
		ML2])

# Extract MOS devices. Device terminal layers *must* exist in
# the extracted view as a result of saveInterconnect.
# In this case we are using pcell devices which will be
# created according to the recognition region polygon.
print "# Extract MOS devices"
extractMOS("nch", ngate, POL, ndiff, PWL)
extractMOS("pch", pgate, POL, pdiff, NWL)
#extractMOS("nch_ex", ngate, polyg, active, psub)

# Extract resistors. Device terminal layers must exist in
# extracted view as a result of saveInterconnect.
#if geomNumShapes(rpo) > 0 :
#	print "# Extract poly resistors"
#	extractRes("rppoly_ex", pres, polyg)

# Extract MOS capacitors. Device terminal layers must exist in
# extracted view as a result of saveInterconnect.
#if geomNumShapes(cap) > 0 :
#	print "# Extract MOS capacitors"
#	extractMosCap("nmoscap_ex", mcap, polyg, active)

# Extract parasitics. 
#extractParasitic(metal1, 1.15e-14, 1.50e-14, "VSS")
#extractParasitic2(metal1, metal2, 2.0e-14, 2.0e-14)
#extractParasitic3D("vss", "vss")

# Exit boolean package, freeing memory
print "# Extraction completed."
geomEnd()

# Open the extracted view
ui.openCellView(lib.libName(), cv.cellName(), "extracted")
