# Kyle Davis 
# Created: Dec 12, 2016

# This basic script acts as a stand-alone bulk field updater. This method is faster than using standard field calculation in ArcMap.

import arcpy

arcpy.env.workspace = r"C:\Users\kydavis\Documents\VistaCity.gdb"

featureClass = r"C:\Users\kydavis\Documents\VistaCity.gdb\zoning"

# List fields to be changed here, refer to arcpy documentation regarding FID shortcuts
fieldList = ["ZoningCode", "DetailDesc"]

def updatefieldtool(curvalue, newvalue, fc=featureClass):
	with arcpy.da.UpdateCursor(fc, fieldList) as updateCursor:
	    for row in updateCursor:
	    	# Select field using the fieldList index
	    	if row[1] == curvalue:        
		       row[0] = newvalue
		       updateCursor.updateRow(row)
	print("The specified values have been updated")


# function calls
updatefieldtool(curvalue='Commercial', newvalue='C-1')

updatefieldtool(curvalue='Residential', newvalue='R-1')

