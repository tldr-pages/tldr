# hdiutil

> Lemezképek létrehozására és kezelésére szolgáló segédprogram. További információ: <https://ss64.com/osx/hdiutil.html>.

- Lemezkép mountolása:

`hdiutil attach {{path/to/image_file}}`

- Lemezkép leválasztása:

`hdiutil detach /Volumes/{{volume_name}}`

- Felcsatolt lemezképek listázása:

`hdiutil info`

- ISO-kép létrehozása egy könyvtár tartalmából:

`hdiutil makehybrid -o {{path/to/output_file}} {{path/to/directory}}`
