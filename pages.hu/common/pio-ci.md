# pio ci

> PlatformIO projektek építése tetszőleges forráskód struktúrával. Ez egy új ideiglenes projektet hoz létre, amelybe a forráskódot bemásolja. További információ: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- Építsen egy PlatformIO projektet a rendszer alapértelmezett ideiglenes könyvtárában, majd törölje azt:

`pio ci {{path/to/project}}`

- Építsen egy PlatformIO projektet, és adjon meg konkrét könyvtárakat:

`pio ci --lib {{path/to/library_directory}} {{path/to/project}}`

- Építsen egy PlatformIO projektet, és adjon meg egy adott lapot (`pio boards` felsorolja az összeset):

`pio ci --board {{board}} {{path/to/project}}`

- PlatformIO projekt építése egy adott könyvtárban:

`pio ci --build-dir {{path/to/build_directory}} {{path/to/project}}`

- Építsen egy PlatformIO projektet, és ne törölje az építési könyvtárat:

`pio ci --keep-build-dir {{path/to/project}}`

- PlatformIO projekt építése egy adott konfigurációs fájl használatával:

`pio ci --project-conf {{path/to/platformio.ini}}`
