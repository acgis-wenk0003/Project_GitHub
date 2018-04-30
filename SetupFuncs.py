import arcpy
#set up functions

def midpointCreation(mapdoc):
    layers= arcpy.ListFeatureClasses()
    for layer in layers:
        print layer
