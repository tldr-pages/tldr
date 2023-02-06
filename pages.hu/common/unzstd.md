# unzstd

> A fájlok Zstandard tömörítéssel történő kicsomagolása. További információ: <https://github.com/facebook/zstd>.

- Fájlok dekompressziója:

`unzstd {{path/to/file1.ztd path/to/file2.ztd ...}}`

- Egy fájl dekompressziója egy adott kimeneti fájlba:

`unzstd {{path/to/compressed.ztd}} -o {{path/to/extracted_file}}`

- A tömörített fájlra vonatkozó információk megjelenítése:

`unzip --list {{path/to/file.zst}}`
