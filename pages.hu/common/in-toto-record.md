# in-toto-record

> Aláírt link metaadatfájl létrehozása az ellátási lánc lépéseihez szükséges bizonyítékok biztosítása érdekében. További információ: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>.

- Indítsa el a rekordot (előzetes linkfájlt hoz létre):

`in-toto-record start -n {{edit-files}} -k {{path/to/key_file}} -m {{.}}`

- A rekord leállítása (előzetes linkfájlt vár):

`in-toto-record stop -n {{edit-files}} -k {{path/to/key_file}} -p {{.}}`
