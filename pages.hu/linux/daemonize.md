# daemonize

> Egy parancs futtatása (amely nem démonizálja magát) Unix-démonként. További információ: <http://software.clapper.org/daemonize/>.

- Parancs futtatása démonként:

`daemonize {{command}} {{command_arguments}}`

- A PID írása a megadott fájlba:

`daemonize -p {{path/to/pidfile}} {{command}} {{command_arguments}}`

- Zárfájl használatával biztosítsa, hogy egyszerre csak egy példány futjon:

`daemonize -l {{path/to/lockfile}} {{command}} {{command_arguments}}`

- Használja a megadott felhasználói fiókot:

`sudo daemonize -u {{user}} {{command}} {{command_arguments}}`
