import arcpy
arcpy.env.workspace = "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04"
arcpy.CreateFileGDB_management(arcpy.env.workspace, "lab04.gdb")
garages = arcpy.management.MakeXYEventLayer("garages.csv", "x", "y",)
