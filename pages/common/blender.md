# blender

> Command-line interface to the Blender 3D computer graphics application.
> Arguments are executed in the order they are given.

- Render all frames of an animation in the background (without UI):

`blender -b {{file.blend}} -a`

- Render an animation to a specific output path relative to the .blend file:

`blender -b {{file.blend}} -o //{{render/frame_###.png}} -a`

- Render the 10th frame of an animation as a single image:

`blender -b {{file.blend}} -f {{10}}`

- Render the second last frame in an animation as a JPEG image:

`blender -b {{file.blend}} -F JPEG -f -2`

- Render the animation of a specific scene, starting at frame 10 and ending at frame 500:

`blender -b {{file.blend}} -S {{scene_name}} -s 10 -e 500 -a`

- Render an animation at a specific resolution, by passing a Python expression:

`blender -b {{file.blend}} --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' -a`

- Start an interactive Blender session in the terminal with a python console (do `import bpy` after starting):

`blender -b --python-console`
