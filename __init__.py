bl_info = {
    "name": "bhcam",
    "author": "ShinagawaKazearu",
    "version": (0,0,2),
    "blender": (3,0),
    "description": "write map info for fixed camera game",
    "support": "TESTING",
    "location": "Properties - Scene",
    "category": "Object",
}

from typing import Set
import imp

import bpy

from . import dump_map

def register():
    imp.reload(dump_map)

    bpy.utils.register_class(dump_map.DumpMap)
    bpy.utils.register_class(dump_map.PROPERTIES_PT_DumpMap)

    print("registered")


def unregister():

    bpy.utils.unregister_class(dump_map.PROPERTIES_PT_DumpMap)
    bpy.utils.unregister_class(dump_map.DumpMap)

    print("unregistered")


if __name__ == "__main__":
    register()
