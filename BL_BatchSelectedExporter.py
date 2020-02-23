import bpy
import os

# get the path where the blend file is located
ExportDir = bpy.path.abspath('C:/Users/peter/Documents/Purpl3grapeLaptop/GitHub/Blender/FlightRunnerLevel/Export2')

def ExportObjectGroupToFBX(objectName):  
    # deselect all objects
    bpy.ops.object.select_all(action='SELECT')
    obsToExport = set()
    # loop through all the objects in the scene
    scene = bpy.context.selected_objects
    for ob in scene:
        # make the current object active and select it
        
        if(ob.name.startswith(objectName)):
            bpy.context.view_layer.objects.active = ob
            bpy.data.objects[ob.name].select_set(True)
            obsToExport.add(bpy.data.objects[ob.name])
        else:
            bpy.data.objects[ob.name].select_set(False)
        #ob.select = True
   
    bpy.ops.export_scene.fbx(filepath=os.path.join(ExportDir, objectName + '.fbx'),use_selection=True,)
    
if __name__ == '__main__':
    ExportObjectGroupToFBX('Loop_A')
    ExportObjectGroupToFBX('Road_A')
    ExportObjectGroupToFBX('Road_B')
    ExportObjectGroupToFBX('Road_C')
    ExportObjectGroupToFBX('Road_D')
    ExportObjectGroupToFBX('Road_E')
    ExportObjectGroupToFBX('Road_Building_01')
