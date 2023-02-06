# isisdl

> Letöltő segédprogram a TU-Berlin ISIS számára. Töltse le az összes fájlt és videót az ISIS-ről. További információ: <https://github.com/Emily3403/isisdl>.

- Indítsa el a szinkronizálási folyamatot:

`isisdl`

- Korlátozza a letöltési sebességet 20 MiB/s-ra, és töltse le 5 szálon:

`isisdl --download-rate {{20}} --max-num-threads {{5}}`

- Futtassa az inicializáló konfigurációs varázslót:

`isisdl --init`

- Futtassa a további konfigurációs varázslót:

`isisdl --config`

- Indítsa el az adatbázis teljes szinkronizálását, és számítsa ki minden fájl ellenőrző összegét:

`isisdl --sync`

- Az ffmpeg elindítása a letöltött videók tömörítéséhez:

`isisdl --compress`
