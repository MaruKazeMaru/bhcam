from typing import Set

import bpy
from bpy.types import Context, Event

def get_string(self):
    return self["filepath"]
def set_string(self, value:str):
    self["filepath"] = value


class DumpMap(bpy.types.Operator):
    bl_idname = "bhcam.dump_map"
    bl_label = "dumpmap"
    bl_description = "write map info as JSON"
    bl_options = {"REGISTER"}

    filepath : bpy.props.StringProperty(
        description="output file path. If only directory name, file name is \"arrangement.json\"",
        default="map.json",
        subtype="FILE_PATH",
    )

    def execute(self, context:bpy.types.Context) -> Set[str] | Set[int]:
        with open(self.filepath, "a") as f:
            f.write("add by bhcam.DumpMap")
        return {"FINISHED"}


    def invoke(self, context: Context, event: Event) -> Set[str] | Set[int]:
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class PROPERTIES_PT_DumpMap(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Dump Map"

    def draw(self, context:bpy.types.Context):
        props = self.layout.operator(DumpMap.bl_idname, text="dump")


# class FILEBROWSER_PT_SetPath(bpy.types.Panel):
#     bl_space_type = "FILE_BROWSER"
#     bl_region_type = "WINDOW"
#     bl_label = "Set Gameobject Arrangement Path"

#     @classmethod
#     def poll(cls, context:bpy.types.Context):

