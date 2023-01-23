# envoy

> PHP-alapú feladatkezelő a Laravel távoli szervereihez. További információ: <https://laravel.com/docs/envoy>.

- Konfigurációs fájl inicializálása:

`envoy init {{host_name}}`

- Egy feladat futtatása:

`envoy run {{task_name}}`

- Feladat futtatása egy adott projektből:

`envoy run --path {{path/to/directory}} {{task_name}}`

- Egy feladat futtatása és folytatása hiba esetén:

`envoy run --continue {{task_name}}`

- Feladat kiürítése Bash scriptként ellenőrzés céljából:

`envoy run --pretend {{task_name}}`

- Csatlakozás a megadott kiszolgálóhoz SSH-n keresztül:

`envoy ssh {{server_name}}`
