# xml2man

> Az MPGL-t mdoc-ba fordítja. További információ: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- MPGL fájl fordítása megtekinthető man page-be:

`xml2man {{path/to/command.mxml}}`

- MPGL-fájl fordítása egy adott kimeneti fájlba:

`xml2man {{path/to/service.mxml}} {{path/to/service.7}}`

- MPGL-fájl fordítása egy adott kimeneti fájlba, felülírva, ha már létezik:

`xml2man -f {{path/to/function.mxml}} {{path/to/function.3}}`
