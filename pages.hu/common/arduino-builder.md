# arduino-builder

> Parancssori eszköz arduino vázlatok fordításához. DEPRECATION WARNING: Ezt az eszközt a `arduino` javára megszüntetjük. További információ: <https://github.com/arduino/arduino-builder>.

- Kompiláljon egy skiccet:

`arduino-builder -compile {{path/to/sketch.ino}}`

- Adja meg a hibakeresési szintet (alapértelmezett: 5):

`arduino-builder -debug-level {{1..10}}`

- Adjon meg egy egyéni építési könyvtárat:

`arduino-builder -build-path {{path/to/build_directory}}`

- Használjon egy build option fájlt, ahelyett, hogy minden alkalommal manuálisan megadná a `--hardware`, `--tools`, stb:

`arduino-builder -build-options-file {{path/to/build.options.json}}`

- Engedélyezze a verbose módot:

`arduino-builder -verbose {{true}}`
