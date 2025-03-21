import os 

import substance_painter.export
import substance_painter.project 
import substance_painter.textureset 
 

plugin_widgets = [] 

def all_textures() :

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


if __name__ == "__main__":
    all_textures()


