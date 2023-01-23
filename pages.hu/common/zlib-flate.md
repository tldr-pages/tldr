# zlib-flate

> Raw zlib tömörítő és dekompressziós program. A `qpdf` része. További információ: <https://manned.org/zlib-flate>.

- Egy fájl tömörítése:

`zlib-flate -compress < {{path/to/input_file}} > {{path/to/compressed.zlib}}`

- Egy fájl kitömörítése:

`zlib-flate -uncompress < {{path/to/compressed.zlib}} > {{path/to/output_file}}`

- Egy fájl tömörítése megadott tömörítési szinttel. 0=A leggyorsabb (legrosszabb), 9=leglassabb (legjobb):

`zlib-flate -compress={{compression_level}} < {{path/to/input_file}} > {{path/to/compressed.zlib}}`
