import arcpy

def __main__():
    arcpy.env.workspace = "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04"
    # arcpy.CreateFileGDB_management("C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/", "DB")
    CSV = "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/garages.csv"
    RIPX = "X"
    RIPY = "Y"
    lol = "garage_points"
    return1 = arcpy.MakeXYEventLayer_management(CSV, RIPX, RIPY, lol)

    garages = "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/garage_points"
    duh = r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb"
    arcpy.FeatureClassToGeodatabase_conversion(return1, duh)

    swag= r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/Campus.gdb/Structures"
    awesome= r"C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/Structures"
    arcpy.Copy_management(swag, awesome)

    
    spatial_ref = arcpy.Describe(awesome).spatialReference
    arcpy.Project_management(garages, "C:/Users/cadet/DevSource/Trahan_GEOG392/lab/lab04/DB.gdb/ProjectGarages", spatial_ref)




if __name__ == '__main__':
    __main__()