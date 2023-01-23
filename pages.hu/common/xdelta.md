# xdelta

> Delta kódoló segédprogram. Gyakran használják foltok bináris fájlokra történő alkalmazásához. További információ: <http://xdelta.org>.

- Folt alkalmazása:

`xdelta -d -s {{path/to/input_file}} {{path/to/delta_file.xdelta}} {{path/to/output_file}}`

- Javítófolt létrehozása:

`xdelta -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/output_file.xdelta}}`
