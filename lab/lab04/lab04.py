import arcpy

def __main__():
    arcpy.env.workspace = "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04"
    # arcpy.CreateFileGDB_management("C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/", "DB")
        #Creation of the Workspace and Database

        #Creation of XY layer from CSV
    CSV = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/garages.csv"
    coordinate1 = "X"
    coordinate2 = "Y"
    garageout = "garage_points"
    return1 = arcpy.MakeXYEventLayer_management(CSV, coordinate1,coordinate2, garageout)

        #Inputting the new XY Layer to the Database
    garages = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/garage_points"
    database = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb"
    arcpy.FeatureClassToGeodatabase_conversion(return1, database)

        #Inputting the Structure Shapefile from the Class Database to the Created Database
    StructuresOld= r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/Campus.gdb/Structures"
    StructuresNew= r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/Structures"
    arcpy.Copy_management(StructuresOld, StructuresOld)

        #The Spatial Reference from the Structures File being appended to the new XY file
    spatial_ref = arcpy.Describe(StructuresOld).spatialReference
    arcpy.Project_management(garages, r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/ProjectGarages", spatial_ref)

        #150m Buffer of the XY file
    projected = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/ProjectGarages"
    BufferLoc = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/BufferGarages"
    return2 = arcpy.Buffer_analysis(projected, BufferLoc, 150)

        #Intersect of the Buffer and Structures Shapefiles
    IntersectLoc = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/IntersectBufferStructures"
    arcpy.Intersect_analysis([BufferLoc, awesome],IntersectLoc, "ALL")

        #Output the Intersect as a new Table
    arcpy.TableToTable_conversion(IntersectLoc, r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04", r"lab04.csv")

if __name__ == '__main__':
    __main__()