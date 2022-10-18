import arcpy
arcpy.env.workspace = "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04"
garages = arcpy.management.MakeXYEventLayer("garages.csv", "x", "y", "garages")
gands = ["Structures.shp", garages]
arcpy.FeatureClassToGeodatabase_conversion(garages, "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/lab04.gdb")
return2 = arcpy.Buffer_analysis(garages, "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/Buffgarages", 150)
Intersect = arcpy.Intersect_analysis(return2 + "Structures.shp", Intersect, ALL) 
arcpy.TableToTable_conversion(Intersect, "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04", finaltable)