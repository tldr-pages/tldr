# swc

> Rust nyelven írt JavaScript és TypeScript fordító. További információ [: https://swc.rs](https://swc.rs).

- Egy megadott bemeneti fájl transzpilezése és kimenete a `stdout`:

`swc {{path/to/file}}`

- Transpile a bemeneti fájl minden egyes módosításakor:

`swc {{path/to/file}} --watch`

- Egy megadott bemeneti fájl transzpilezése és kimenet egy adott fájlba:

`swc {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Transpile egy megadott bemeneti könyvtár és kimenet egy adott könyvtárba:

`swc {{path/to/input_directory}} --out-dir {{path/to/output_directory}}`

- Egy megadott bemeneti könyvtár átfordítása egy adott konfigurációs fájl segítségével:

`swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}`

- A glob path segítségével megadott könyvtárban lévő fájlok figyelmen kívül hagyása:

`swc {{path/to/input_directory}} --ignore {{ignored_files}}`
