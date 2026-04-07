"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)


tree_trunk_height = 5
tree_trunk_radius = 0.5
tree_trunk_x = 2
tree_trunk_z = 3

tree_trunk = cmds.polyCylinder(
    name="tree_trunk_01",
    height=tree_trunk_height,
    radius=tree_trunk_radius,
)[0]

cmds.move(tree_trunk_x, tree_trunk_height / 2.0, tree_trunk_z, tree_trunk)



tree_top_radius = 2
tree_top_x = tree_trunk_x
tree_top_z = tree_trunk_z

tree_top = cmds.polySphere(
    name="tree_top_01",
    radius=tree_top_radius,
)[0]

# Place it on top of the trunk
cmds.move(tree_top_x, tree_trunk_height + tree_top_radius, tree_top_z, tree_top)


building2_width = 3
building2_height = 4
building2_depth = 3
building2_x = 6
building2_z = -4

building2 = cmds.polyCube(
    name="building_02",
    width=building2_width,
    height=building2_height,
    depth=building2_depth,
)[0]

cmds.move(building2_x, building2_height / 2.0, building2_z, building2)


cone_height = 3
cone_radius = 1.5
cone_x = building2_x
cone_z = building2_z

cone = cmds.polyCone(
    name="roof_cone_01",
    height=cone_height,
    radius=cone_radius,
)[0]

# Place it on top of building 2
cmds.move(cone_x, building2_height + (cone_height / 2.0), cone_z, cone)

# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
