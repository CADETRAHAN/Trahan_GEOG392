import arcpy
import os
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True

#Data Input and Output
Well_Input = arcpy.GetParameter(0)
Power_Line_Input = arcpy.GetParameter(1)
Irradiance_Raster = arcpy.GetParameter(2)
Profit_Wells = arcpy.GetParameter(3)

#Mathmatic Expressions for Profit Calculation
Expression = "!GROSS_PROFIT! - !TOTAL_COST!"
Meters2Miles = "(!NEAR_DIST!/1609.34)"
Spur_Cost = "(!DIST_MILES!*847000)"
Total_Cost = "(1481000 + !SPUR_COST!)"
Zero_Distance_Profit = "(!RASTERVALU! * 524464.2)"

#Finding the Irradiance per Well Site and making a new Feature Class
try:
    ExtractValuesToPoints(Well_Input, Irradiance_Raster, Profit_Wells)
except: 
    print(arcpy.GetMessages())

#Mathmatics of Cost Including Finding the Nearest Distance from a Well to a Power Line
try:
    arcpy.Near_analysis(Profit_Wells, Power_Line_Input, "Miles", "NO_LOCATION", "NO_ANGLE", "GEODESIC")
    arcpy.CalculateField_management(Profit_Wells, "DIST_MILES", Meters2Miles, None, None, "FLOAT")
    arcpy.CalculateField_management(Profit_Wells, "SPUR_COST", Spur_Cost, None, None, "FLOAT")
    arcpy.CalculateField_management(Profit_Wells, "TOTAL_COST", Total_Cost, None, None, "FLOAT")
    arcpy.CalculateField_management(Profit_Wells, "GROSS_PROFIT", Zero_Distance_Profit, None, None, "FLOAT")
    arcpy.CalculateField_management(Profit_Wells, "Net_Profit", Expression, None, None, "FLOAT")
except:
    print(arcpy.GetMessages())
