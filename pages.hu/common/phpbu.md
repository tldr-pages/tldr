# phpbu

> Biztonsági mentési segédprogram keretrendszer PHP-hez. További információ: <https://phpbu.de>.

- Biztonsági mentések futtatása az alapértelmezett `phpbu.xml` konfigurációs fájl használatával:

`phpbu`

- Biztonsági mentések futtatása egy adott konfigurációs fájl használatával:

`phpbu --configuration={{path/to/configuration_file.xml}}`

- Csak a megadott biztonsági mentések futtatása:

`phpbu --limit={{backup_task_name}}`

- Szimulálja a végrehajtott műveleteket:

`phpbu --simulate`
