import bpy

bl_info = {
    "name": "bhcam",
    "author": "ShinagawaKazearu",
    "version": (0,0),
    "blender": (3,0),
    "description": "write map info for fixed camera game",
    "support": "TESTING",
    "category": "Object",
}

def register():
    print("registered")


def unregister():
    print("unregistered")


if __name__ == "__main__":
    register()
