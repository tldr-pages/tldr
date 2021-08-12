# parquet-tools

> Un instrument pentru afișarea, inspectarea și manipularea fișierului Parchet.
> Mai multe informaţii: <https://github.com/apache/parquet-mr/tree/master/parquet-tools-deprecated>

- Afișează conținutul unui fișier Parchet:

`parquet-tools cat {{path/to/parquet}}`

- Afișează primele câteva linii ale unui fișier Parchet:

`parquet-tools head {{path/to/parquet}}`

- Imprimați schema unui fișier Parchet:

`parquet-tools schema {{path/to/parquet}}`

- Imprimați metadatele unui fișier Parchet:

`parquet-tools meta {{path/to/parquet}}`

- Imprimați conținutul și metadatele unui fișier Parchet:

`parquet-tools dump {{path/to/parquet}}`

- Concatenează mai multe fișiere Parchet în cel țintă:

`parquet-tools merge {{path/to/parquet1}} {{path/to/parquet2}} {{path/to/target_parquet}}`

- Imprimați numărul de rânduri într-un fișier Parchet:

`parquet-tools rowcount {{path/to/parquet}}`

- Imprimați coloana și indexurile de offset ale unui fișier Parchet:

`parquet-tools column-index {{path/to/parquet}}`
