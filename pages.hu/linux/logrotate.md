# logrotate

> Forgatja, tömöríti és postázza a rendszernaplókat. További információ: <https://manned.org/logrotate>.

- Futtatás indítása manuálisan:

`logrotate {{path/to/logrotate.conf}} --force`

- Futtatás egy adott parancs segítségével a jelentések postázásához:

`logrotate {{path/to/logrotate.conf}} --mail {{/usr/bin/mail_command}}`

- Futtatás állapot (lock) fájl használata nélkül:

`logrotate {{path/to/logrotate.conf}} --state /dev/null`

- Futtatás és az állapot (lock) fájl ellenőrzésének kihagyása:

`logrotate {{path/to/logrotate.conf}} --skip-state-lock`

- A `logrotate` megadása a verbózus kimenet naplófájlba történő naplózására:

`logrotate {{path/to/logrotate.conf}} --log {{path/to/log_file}}`
