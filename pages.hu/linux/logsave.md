# logsave

> A parancs kimeneti adatainak naplófájlba mentése. További információ: <https://manned.org/logsave>.

- Parancs végrehajtása a megadott argumentum(ok)kal, és a kimenet mentése naplófájlba:

`logsave {{path/to/logfile}} {{command}}`

- Bemenet felvétele a standard bemenetről és mentése egy naplófájlba:

`logsave {{logfile}} -`

- A kimenet hozzáadása egy naplófájlhoz, ahelyett, hogy helyettesítené annak aktuális tartalmát:

`logsave -a {{logfile}} {{command}}`

- Szöveges kimenet megjelenítése:

`logsave -v {{logfile}} {{command}}`
