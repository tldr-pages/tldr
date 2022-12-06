# blender

> Command-line interface to the Blender 3D computer graphics application.
> Arguments are executed in the order they are given.
> More information: <https://manned.org/blender>.

- Render all frames of an animation in the background, without loading the UI (output is saved to `/tmp`):

`blender --background {{path/to/file}}.blend --render-anim`

- Render an animation using a specific image naming pattern, in a path relative (`//`) to the .blend file:

`blender --background {{path/to/file}}.blend --render-output //{{render/frame_###.png}} --render-anim`

- Render the 10th frame of an animation as a single image, saved to an existing directory (absolute path):

`blender --background {{path/to/file}}.blend --render-output {{/path/to/output_directory}} --render-frame {{10}}`

- Render the second last frame in an animation as a JPEG image, saved to an existing directory (relative path):

`blender --background {{path/to/file}}.blend --render-output //{{output_directory}} --render-frame {{JPEG}} --render-frame {{-2}}`

- Render the animation of a specific scene, starting at frame 10 and ending at frame 500:

`blender --background {{path/to/file}}.blend --scene {{scene_name}} --frame-start {{10}} -e {{500}} --render-anim`

- Render an animation at a specific resolution, by passing a Python expression:

`blender --background {{path/to/file}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' --render-anim`

- Start an interactive Blender session in the terminal with a python console (do `import bpy` after starting):

`blender --background --python-console`
