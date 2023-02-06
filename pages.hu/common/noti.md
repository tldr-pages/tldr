# noti

> Folyamat figyelése és banner-értesítés indítása. További információ: <https://github.com/variadico/noti>.

- Értesítés megjelenítése, amikor a tar befejezi a fájlok tömörítését:

`noti {{tar -cjf example.tar.bz2 example/}}`

- Értesítés megjelenítése akkor is, ha a megfigyelendő parancs után helyezi el:

`{{command_to_watch}}; noti`

- Egy folyamat figyelése PID szerint, és értesítés indítása, ha a PID eltűnik:

`noti -w {{process_id}}`
