import arcpy
import os
import SetupFuncs as setup
mxd= arcpy.mapping.MapDocument("..\..\Project_Tinkering.mxd")
townships=["Loyalist", "GreaterNapanee", "AddingtonHighlands", "StoneMills"]

setup.midpointCreation(mxd)

