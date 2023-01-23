# soupault

> A Soupault egy statikus weboldal generátor, amely a HTML elemfa átírásán alapul. HTML post-processzorként vagy metaadat-kivonatként is használható. További információ: <https://soupault.app>.

- Egy minimális weboldal projekt inicializálása az aktuális munkakönyvtárban:

`soupault --init`

- Hozzon létre egy weboldalt:

`soupault`

- Az alapértelmezett konfigurációs fájlok és könyvtárak helyének felülírása:

`soupault --config {{config_path}} --site-dir {{input_dir}} --build-dir {{output_dir}}`

- Metaadatok kivonása JSON fájlba oldalak generálása nélkül:

`soupault --index-only --dump-index-json {{path/to/file.json}}`

- A tényleges konfiguráció megjelenítése (a `soupault.toml` oldal értékei plusz az alapértelmezettek):

`soupault --show-effective-config`
