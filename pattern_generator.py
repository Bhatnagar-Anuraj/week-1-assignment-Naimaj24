"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern():
    """Generate a procedural pattern of objects using nested loops.

    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
    # --- Configuration variables ---
    num_rows = 5        # Number of rows in the pattern.
    num_cols = 5        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.

    # TODO: Create a nested loop that iterates over rows and columns.
    
    # --- Nested loop to create grid ---
    for row in range(num_rows):
        for col in range(num_cols):

            # Calculate position based on grid
            x_position = col * spacing
            z_position = row * spacing

            # --- Conditional logic for pattern ---
            # Alternate between cube and sphere
            if (row + col) % 2 == 0:
                object_size = 1.5
                new_object = cmds.polyCube(
                    name=f"cube_{row}_{col}",
                    width=object_size,
                    height=object_size,
                    depth=object_size
                )[0]

            else:
                object_size = 1.0
                new_object = cmds.polySphere(
                    name=f"sphere_{row}_{col}",
                    radius=object_size
                )[0]

            # --- Position object ---
            # Raise object so it sits on ground
            y_position = object_size / 2.0
            cmds.move(x_position, y_position, z_position, new_object)

            # --- Optional scaling variation ---
            # Make every third object taller
            if (row * col) % 3 == 0:
                cmds.scale(1, 2, 1, new_object)




# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
