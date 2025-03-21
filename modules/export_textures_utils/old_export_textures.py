import os 
import substance_painter.textureset 


def export_textures(stack):
 
 material = stack.material()
 
 export_preset = substance_painter.resource.ResourceID( 
      context="starter_assets", 
      name="PBR Metallic Roughness" )
 
 print( "Preset: " + export_preset.url() ) 

 Path = substance_painter.project.file_path() 
 Path = os.path.dirname(Path) + "/"

 config = { 
  "exportShaderParams"  : False, 
  "exportPath"    : Path, 
  "exportList"   : [ { "rootPath" : str(stack) } ], 
  "exportPresets"   : [ { "name" : "default", "maps" : [] } ], 
  "defaultExportPreset"  : export_preset.url(), 
  "exportParameters"   : [ 
   { 
    "parameters" : { "paddingAlgorithm": "infinite" } 
   } 
  ] 
 } 

 substance_painter.export.export_project_textures( config ) 