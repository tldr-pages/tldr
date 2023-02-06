# godot

> Nyílt forráskódú 2D és 3D játékmotor. További információ: <https://godotengine.org/>.

- Futtasson egy projektet, ha az aktuális könyvtár tartalmaz egy `project.godot` fájlt, egyébként nyissa meg a projektkezelőt:

`godot`

- Szerkesszen egy projektet (az aktuális könyvtárnak tartalmaznia kell egy `project.godot` fájlt):

`godot -e`

- Nyissa meg a projektkezelőt akkor is, ha az aktuális könyvtár tartalmaz egy `project.godot` fájlt:

`godot -p`

- Egy projekt exportálása egy adott exportálási előbeállításhoz (az előbeállításnak meg kell lennie a projektben):

`godot --export {{preset}} {{output_path}}`

- Önálló GDScript fájl végrehajtása (a szkriptnek a `SceneTree` vagy a `MainLoop` oldalról kell örökölnie):

`godot -s {{script.gd}}`
