# mkisofs

> ISO-fájlok létrehozása könyvtárakból. Más néven `genisoimage`. További információ: <https://manned.org/mkisofs>.

- ISO fájl létrehozása egy könyvtárból:

`mkisofs -o {{filename.iso}} {{path/to/source_directory}}`

- A lemezcímke beállítása ISO létrehozásakor:

`mkisofs -o {{filename.iso}} -V "{{label_name}}" {{path/to/source_directory}}`
