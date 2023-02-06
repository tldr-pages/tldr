# http-server-upload

> Konfigurációmentes parancssori HTTP-kiszolgáló, amely könnyű felületet biztosít fájlok feltöltéséhez. További információ: <https://github.com/crycode-de/http-server-upload>.

- Indítson el egy HTTP-kiszolgálót az alapértelmezett porton, hogy fájlokat töltsön fel az aktuális könyvtárba:

`http-server-upload`

- HTTP-kiszolgáló indítása a feltöltéshez megadott maximálisan megengedett fájlmérettel MiB-ban (alapértelmezett érték 200 MiB):

`MAX_FILE_SIZE={{size_in_megabytes}} http-server-upload`

- HTTP-kiszolgáló indítása egy adott porton fájlok feltöltéséhez az aktuális könyvtárba:

`PORT={{port}} http-server-upload`

- HTTP-kiszolgáló indítása, a feltöltött fájlok tárolása egy adott könyvtárban:

`UPLOAD_DIR={{path/to/directory}} http-server-upload`

- HTTP-kiszolgáló indítása egy adott könyvtár használatával a fájlok ideiglenes tárolására a feltöltési folyamat során:

`UPLOAD_TMP_DIR={{path/to/directory}} http-server-upload`

- HTTP-kiszolgáló indítása, amely a feltöltéseket a HTTP-üzenetben megadott token-mezővel fogadja el:

`TOKEN={{secret}} http-server-upload`
