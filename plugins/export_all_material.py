import os 

import substance_painter.ui 
import substance_painter.export 
import substance_painter.project 
import substance_painter.textureset 
 
from PySide6 import QtGui


plugin_widgets = [] 

# -----------------------------------------------------------------------------------
def export_all_textures() : 
    if not substance_painter.project.is_open() : 
        return 

    texture_sets = substance_painter.textureset.all_texture_sets()

    export_preset = substance_painter.resource.ResourceID( 
      context="starter_assets", 
      name="PBR Metallic Roughness" )
    
    print( "Preset:" ) 
    print( export_preset.url() ) 


    Path = substance_painter.project.file_path() 
    Path = os.path.dirname(Path) + "/"


    export_list = [] 
    
    # Iterate through each texture set and print its name and Export all texture sets
    for texture_set in texture_sets:
        print(texture_set.name)
        export_list.append({"rootPath": texture_set.name})
    
    

    config = { 
    "exportShaderParams"  : False, 
    "exportPath"    : Path, 
    "exportList"   : export_list , 
    "exportPresets"   : [ { "name" : "default", "maps" : [] } ], 
    "defaultExportPreset"  : export_preset.url(), 
        "exportParameters"   : [ 
            { 
                "parameters" : { "paddingAlgorithm": "infinite" } 
            } 
        ] 
    }  
    substance_painter.export.export_project_textures( config ) 
   

    


# -----------------------------------------------------------------------------------
def start_plugin():
    Action = QtGui.QAction("Export All Materials", triggered=export_all_textures)

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