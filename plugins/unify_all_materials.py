import os 

import substance_painter.ui 
import substance_painter.export 
import substance_painter.project 
import substance_painter.textureset 

from PySide6 import QtGui

plugin_widgets = [] 

# -----------------------------------------------------------------------------------
def export_all_materials() : 

    Path = substance_painter.project.file_path() 
    Path = os.path.dirname(Path) + "/"  

    texture_sets = substance_painter.textureset.all_texture_sets()

    export_preset = substance_painter.resource.ResourceID( 
      context="starter_assets", 
      name="Unity HD Render Pipeline (Metallic Standard)" )
    
    # export_preset = substance_painter.resource.ResourceID( 
    #   context="starter_assets", 
    #   name="TRANSPARENT Unity HD Render Pipeline")
    
    print( "Preset:" ) 
    print( export_preset.url() ) 

    export_list = [] 
    
    # Iterate through each texture and Export all texture sets
    for texture_set in texture_sets:
        export_list.append({"rootPath": texture_set.name})

    config = { 
    "exportShaderParams"  : False, 
    "exportPath"    : Path, 
    "exportList"   : export_list , 
    "exportPresets"   : [ { "name" : "default", "maps" : [] } ], 
    "defaultExportPreset"  : export_preset.url(), 
        "exportParameters"   : [ 
            { 
                "parameters" : { "paddingAlgorithm": "transparent", "dilationDistance" : 16 } 
            } 
        ] 
    }  

    substance_painter.export.export_project_textures( config ) 

# -----------------------------------------------------------------------------------
def unify_all_materials():

    Path = substance_painter.project.file_path() 
    Path = os.path.dirname(Path) + "/"  

    list_channels = []
    list_images = []

    image_directory = Path #directory_path 
    image_files = [f for f in os.listdir(image_directory) if f.endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]

    # Read each image
    for image_file in image_files:
        
        list_images.append(image_file)

        string = image_file
        last_dot_index = string.rfind(".")
        substring = string[:last_dot_index]
        name_channel = substring.split('_')[-1]

        list_channels.append(name_channel)
    
    unique_list = list(set(list_channels))
    list_channels = {item: [] for item in unique_list}

    # print(list_channels)
    # print(list_images)

    # Iterate over the list of images
    for image in list_images:
       
        # Split the filename to get parts
        parts = image.split('_')
        channel_type = parts[-1].split('.')[0]  # Extract the channel type (BaseMap, MaskMap, Normal)

        # Append the image to the correct channel list
        list_channels[channel_type].append(image)



# -----------------------------------------------------------------------------------
def create_menu() :
    if not substance_painter.project.is_open() : 
        return 

    export_all_materials()
    unify_all_materials()

# -----------------------------------------------------------------------------------
def start_plugin():
    Action = QtGui.QAction("Unify all Materials", triggered=create_menu)

    substance_painter.ui.add_action( substance_painter.ui.ApplicationMenu.File, Action ) 

    plugin_widgets.append(Action) 

# -----------------------------------------------------------------------------------
def close_plugin(): 
 for widget in plugin_widgets: 
  substance_painter.ui.delete_ui_element(widget) 
 
 plugin_widgets.clear() 

# -----------------------------------------------------------------------------------
if __name__ == "__main__": 
 start_plugin()