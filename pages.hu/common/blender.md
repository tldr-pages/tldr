# blender

> A Blender 3D számítógépes grafikai alkalmazás parancssori interfésze. Az argumentumok a megadott sorrendben kerülnek végrehajtásra. További információk: <https://manned.org/blender>.

- Egy animáció összes képkockájának a háttérben történő renderelése, a felhasználói felület betöltése nélkül (a kimenet a `/tmp` címre kerül mentésre):

`blender --background {{path/to/file}}.blend --render-anim`

- Animáció renderelése egy adott képnévmintát használva, a .blend fájlhoz relatív (`//`) elérési útvonalon:

`blender --background {{path/to/file}}.blend --render-output //{{render/frame_###.png}} --render-anim`

- Egy animáció 10. képkockájának egyetlen képként történő megjelenítése, egy meglévő könyvtárba mentve (abszolút elérési út):

`blender --background {{path/to/file}}.blend --render-output {{/path/to/output_directory}} --render-frame {{10}}`

- Az animáció utolsó előtti képkockájának renderelése JPEG-ként, egy meglévő könyvtárba mentve (relatív elérési út):

`blender --background {{path/to/file}}.blend --render-output //{{output_directory}} --render-frame {{JPEG}} --render-frame {{-2}}`

- Egy adott jelenet animációjának renderelése a 10. képkockától az 500. képkockáig:

`blender --background {{path/to/file}}.blend --scene {{scene_name}} --frame-start {{10}} -e {{500}} --render-anim`

- Animáció renderelése egy adott felbontásban, egy Python-kifejezés átadásával:

`blender --background {{path/to/file}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' --render-anim`

- Interaktív Blender munkamenet indítása a terminálban egy python konzollal (indítás után tegye meg a `import bpy` címet):

`blender --background --python-console`
