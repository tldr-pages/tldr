# lipo

> Tool voor het verwerken van Mach-O Universal Binaries.
> Meer informatie: <https://keith.github.io/xcode-man-pages/lipo.1.html>.

- Maak een universeel bestand uit twee bestanden met één architectuur:

`lipo {{pad/naar/binary_bestand.x86_64}} {{pad/naar/binary_bestand.arm64e}} -create -output {{pad/naar/binary_bestand}}`

- Toon alle architecturen die een universeel bestand bevat:

`lipo {{pad/naar/binary_bestand}} -archs`

- Toon gedetailleerde informatie over een universeel bestand:

`lipo {{pad/naar/binary_bestand}} -detailed_info`

- Pak een bestand met één architectuur uit uit een universeel bestand:

`lipo {{pad/naar/binary_bestand}} -thin {{arm64e}} -output {{pad/naar/binary_bestand.arm64e}}`
