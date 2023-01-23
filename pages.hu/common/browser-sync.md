# browser-sync

> Helyi webkiszolgálót indít, amely frissíti a böngészőt a fájlváltozásokra. További információ: <https://browsersync.io/docs/command-line>.

- Kiszolgáló indítása egy adott könyvtárból:

`browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}`

- Kiszolgáló indítása helyi könyvtárból, figyelve a könyvtárban található összes CSS-fájlt:

`browser-sync start --server --files '{{path/to/directory/*.css}}'`

- Konfigurációs fájl létrehozása:

`browser-sync init`

- Böngésző-szinkronizálás indítása konfigurációs fájlból:

`browser-sync start --config {{config_file}}`
