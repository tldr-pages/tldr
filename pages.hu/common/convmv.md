# convmv

> A fájlnevek (NEM a fájlok tartalma) egyik kódolásból a másikba való átalakítása. További információ: <https://www.j3e.de/linux/convmv/man/>.

- Tesztelje a fájlnév-kódolás átalakítását (ne változtassa meg a fájlnevet):

`convmv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Állítsa át a fájlnév kódolását, és nevezze át a fájlt az új kódolásra:

`convmv -f {{from_encoding}} -t {{to_encoding}} --notest {{input_file}}`
