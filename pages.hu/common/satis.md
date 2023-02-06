# satis

> A Satis static Composer tároló parancssori segédprogramja. További információ: <https://github.com/composer/satis>.

- Satis konfiguráció inicializálása:

`satis init {{satis.json}}`

- VCS-tár hozzáadása a Satis konfigurációhoz:

`satis add {{repository_url}}`

- A statikus kimenet létrehozása a konfigurációból:

`satis build {{satis.json}} {{path/to/output_directory}}`

- A statikus kimenet építése csak a megadott tároló frissítésével:

`satis build --repository-url {{repository_url}} {{satis.json}} {{path/to/output_directory}}`

- Használhatatlan archívumfájlok eltávolítása:

`satis purge {{satis.json}} {{path/to/output_directory}}`
