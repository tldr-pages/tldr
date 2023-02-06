# lnav

> Fejlett naplófájl megtekintő a naplófájlok elemzéséhez kevés beállítással. További információ: <https://docs.lnav.org/en/latest/cli.html>.

- Egy program naplófájljainak megtekintése naplófájlok, könyvtárak vagy URL-címek megadásával:

`lnav {{path/to/log_or_directory|url}}`

- Egy adott távoli állomás naplóinak megtekintése (SSH jelszó nélküli bejelentkezés szükséges):

`lnav {{ssh}} {{user}}@{{host1.example.com}}:{{/var/log/syslog.log}}`

- A naplófájlok formátumának ellenőrzése a konfigurációval szemben, és az esetleges hibák jelentése:

`lnav -C {{path/to/log_directory}}`
