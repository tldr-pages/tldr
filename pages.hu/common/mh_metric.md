# mh_metric

> Kódmetrikák kiszámítása és érvényesítése MATLAB vagy Octave kódhoz. További információ: <https://misshit.org>.

- Kinyomtatja a kódmetrikákat a megadott fájlokra:

`mh_metric {{path/to/file1.m path/to/file2.m ...}}`

- A megadott Octave-fájlok kódmetrikáinak nyomtatása:

`mh_metric --octave {{path/to/file1.m path/to/file2.m ...}}`

- A megadott könyvtár kódmetrikáinak rekurzív nyomtatása:

`mh_metric {{path/to/directory}}`

- Az aktuális könyvtár kódmetrikáinak nyomtatása:

`mh_metric`

- A kódmetrikai jelentés nyomtatása HTML vagy JSON formátumban:

`mh_metric --{{html|json}} {{path/to/output_file}}`
