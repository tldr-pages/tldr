# snakefmt

> Snakemake fájlok formázása. További információ: <https://github.com/snakemake/snakefmt>.

- Egy adott Snakefile formázása:

`snakefmt {{path/to/snakefile}}`

- Egy adott könyvtárban lévő összes Snakefile rekurzív formázása:

`snakefmt {{path/to/directory}}`

- Egy fájl formázása egy adott konfigurációs fájl segítségével:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Egy fájl formázása egy adott maximális sorhosszúsággal:

`snakefmt --line-length {{100}} {{path/to/snakefile}}`

- A módosítások végrehajtása nélkül végrehajtott változtatások megjelenítése (dry-run):

`snakefmt --diff {{path/to/snakefile}}`
