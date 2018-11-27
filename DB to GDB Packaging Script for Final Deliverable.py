import arcpy, os, shutil
from datetime import datetime

workorderList = [

'WORKORDER_005',
'MAIN_STREET_156',
'MAPLE_STREET_986',
'ELMER_AVE_343',
'EAST_BLVD_258',
'BAYSIDE_STREET_785',
'WELLINGTON_AVE_952',

]



last = str(len(workorderList))
print('Started at {}'.format(str(datetime.now())))

for workorder in workorderList:

    workorderid2 = 'SNF_' + workorder
    # need to automate the export date
    exportdate = '_11_27_18'
    lyrlist = [r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Attachment',
               r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\buildingfootprint',
               r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\equipment',
               r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Span',
               r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\SpliceClosure',
               r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Structure',
               r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\transmedia']




    # create new scratch gdb
    arcpy.CreateFileGDB_management("C:/Users/kydavis/Desktop/workspace/python", "test" + workorder + ".gdb")

    ## Export data from server
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.structure_access_point",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb",
        out_name="structure_access_point",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.transmedia",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="transmedia",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.structure_building",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb",
        out_name="structure_building", where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.structure_poles",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="structure_poles",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.structure_tower",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="structure_tower",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.aerial_span",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="aerial_span",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.gspan",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="gspan",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.lspan",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="lspan",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.tspan",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="tspan",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.attachment_aerial_slack",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb",
        out_name="attachment_aerial_slack",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.attachment_underground_slack",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb",
        out_name="attachment_underground_slack",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.buildingfootprint",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb",
        out_name="buildingfootprint", where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.splice_closure_theoreticalsplice",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb",
        out_name="splice_closure_theoreticalsplice",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.equipment",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="equipment",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")
    arcpy.FeatureClassToFeatureClass_conversion(
        in_features="C:/Users/kydavis/AppData/Roaming/ESRI/Desktop10.6/ArcCatalog/Connection to #.#.#.##.sde/PostgreSQLDB.SanDiego.splice_closure",
        out_path="C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb", out_name="splice_closure",
        where_clause="workorderid ILIKE '%{}%' and isdeleted = 'f'".format(workorder),
        # field mapping info removed, add back or used field mapping object
        field_mapping="",
        config_keyword="")

    ## Merge layers
    # attachment
    arcpy.Merge_management(
        [r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\attachment_aerial_slack',
         r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\attachment_underground_slack'],
        r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Attachment')

    # structure
    arcpy.Merge_management(
        [r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\structure_access_point',
         r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\structure_building',
         r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\structure_poles',
         r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\structure_tower'],
        r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Structure')

    # spliceclosure
    arcpy.Merge_management([r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\splice_closure',
                            r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\splice_closure_theoreticalsplice'],
                           r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\SpliceClosure')

    # span
    arcpy.Merge_management([r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\aerial_span',
                            r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\gspan',
                            r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\lspan',
                            r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\tspan'],
                           r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Span')
    arcpy.CalculateField_management(
        in_table=r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Span',
        field="innerductcount", expression="None", expression_type="PYTHON_9.3", code_block="")

    # arcpy.CalculateField_management(in_table=r'C:\Users\kydavis\Desktop\workspace\python\test' + workorder + r'.gdb\Equipment', field="OUTPUTPORTS", expression="432", expression_type="PYTHON", code_block="")

    ## Change field values
    for layer in lyrlist:
        arcpy.CalculateField_management(in_table=layer, field="isdeleted", expression="None",
                                        expression_type="PYTHON_9.3", code_block="")
        arcpy.CalculateField_management(in_table=layer, field="OPERATION_TYPE", expression="None",
                                        expression_type="PYTHON_9.3", code_block="")
        arcpy.CalculateField_management(in_table=layer, field="WORKORDERID", expression="'{}'".format(workorderid2),
                                        expression_type="PYTHON_9.3", code_block="#")

    # copy template GDB with workorderid name
    arcpy.env.workspace = "C:/Users/kydavis/Desktop/workspace"
    arcpy.Copy_management("C:/Users/kydavis/Desktop/workspace/templates/LLD_GDB_10_25_2017_FromWLS.gdb",
                          "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb")


    arcpy.Append_management(lyrlist[0], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "Attachment"), "NO_TEST")



    arcpy.Append_management(lyrlist[1], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "BuildingFootPrint"), "NO_TEST")


    arcpy.Append_management(lyrlist[2], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "Equipment"), "NO_TEST")


    arcpy.Append_management(lyrlist[3], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "Span"), "NO_TEST")


    arcpy.Append_management(lyrlist[4], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "SpliceClosure"), "NO_TEST")


    arcpy.Append_management(lyrlist[5], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "Structure"), "NO_TEST")


    arcpy.Append_management(lyrlist[6], os.path.join(
        "C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset",
        "Transmedia"), "NO_TEST")

    arcpy.AlterAliasName(
        r"C:/Users/kydavis/Desktop/workspace/deliverables/LLD" + os.sep + workorderid2 + "_LLD" + exportdate + ".gdb" + os.sep + "Dataset/Attachment",
        'MaintenanceLoop')

    print(workorderid2 + " gdb created.")


    print(workorder + " / " + last + " complete")


    # delete scratch gdb
    if arcpy.Exists("C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb"):
        arcpy.Delete_management("C:/Users/kydavis/Desktop/workspace/python/test" + workorder + ".gdb")

endtime = str(datetime.now())

print('Finished at ' + endtime)

