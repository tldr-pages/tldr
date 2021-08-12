# blender

> Interfață linie de comandă pentru aplicația grafică 3D Blender.
> Argumentele sunt executate în ordinea în care sunt date.
> Mai multe informaţii: <https://docs.blender.org/manual/en/latest/advanced/command_line/>

- Randați toate cadrele unei animații în fundal, fără a încărca interfața cu utilizatorul (ieșirea este salvată în `/tmp`):

`blender -b {{filename}}.blend -a`

- Randarea unei animații utilizând un anumit model de denumire a imaginii, într-o cale relativă (`//`) la fișierul.blend:

`blender -b {{filename}}.blend -o //{{render/frame_###.png}} -a`

- Randarea celui de-al 10-lea cadru al unei animații ca o singură imagine, salvată într-un director existent (cale absolută):

`blender -b {{filename}}.blend -o {{/path/to/output_directory}} -f {{10}}`

- Randați al doilea ultim cadru dintr-o animație ca imagine JPEG, salvată într-un director existent (cale relativă):

`blender -b {{filename}}.blend -o //{{output_directory}} -F {{JPEG}} -f {{-2}}`

- Randați animația unei anumite scene, începând de la cadrul 10 și terminând la cadrul 500:

`blender -b {{filename}}.blend -S {{scene_name}} -s {{10}} -e {{500}} -a`

- Randarea unei animații la o anumită rezoluție, prin trecerea unei expresii Python:

`blender -b {{filename}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' -a`

- Începeți o sesiune Blender interactiv în terminal cu o consolă python (efectuați `importați bpy` după pornire):

`blender -b --python-console`
