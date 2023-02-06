# lipo

> A Mach-O univerzális binárisok kezelésére szolgáló eszköz. További információ: <https://ss64.com/osx/lipo.html>.

- Univerzális fájl létrehozása két egyarchitektúrás fájlból:

`lipo {{path/to/binary.x86_64}} {{path/to/binary.arm64e}} -create -output {{path/to/binary}}`

- Az univerzális fájlban található összes architektúra felsorolása:

`lipo {{path/to/binary}} -archs`

- Részletes információk megjelenítése egy univerzális fájlról:

`lipo {{path/to/binary}} -detailed_info`

- Egyetlen architektúrájú fájl kivonása egy univerzális fájlból:

`lipo {{path/to/binary}} -thin {{arm64e}} -output {{path/to/binary.arm64e}}`
