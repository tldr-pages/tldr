# svgr

> SVG-k átalakítása React komponensekké. További információ: <https://react-svgr.com>.

- SVG fájl átalakítása React komponenssé a `stdout` oldalon:

`svgr -- {{path/to/file.svg}}`

- SVG fájl átalakítása React komponenssé TypeScript segítségével a `stdout`:

`svgr --typescript -- {{path/to/file.svg}}`

- SVG fájl átalakítása React komponenssé JSX transzformációval a `stdout`:

`svgr --jsx-runtime automatic -- {{path/to/file.svg}}`

- Egy könyvtár összes SVG fájljának átalakítása React komponensekké egy adott könyvtárba:

`svgr --out-dir {{path/to/output_directory}} {{path/to/input_directory}}`

- Egy könyvtárból az összes SVG fájlt React komponensekké alakítja át egy adott könyvtárba, kihagyva a már átalakított fájlokat:

`svgr --out-dir {{path/to/output_directory}} --ignore-existing {{path/to/input_directory}}`

- Az összes SVG-fájlt egy könyvtárból React komponensekbe transzformálni egy adott könyvtárba, a fájlnevek különleges esetének használatával:

`svgr --out-dir {{path/to/output_directory}} --filename-case {{camel|kebab|pascal}} {{path/to/input_directory}}`

- Az összes SVG-fájlt egy könyvtárból React komponensekké alakítja át egy adott könyvtárba indexfájl generálása nélkül:

`svgr --out-dir {{path/to/output_directory}} --no-index {{path/to/input_directory}}`
