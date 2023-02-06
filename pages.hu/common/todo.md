# todo

> Egy egyszerű, szabványokon alapuló, klienses todo manager. További információ: <https://todoman.readthedocs.io>.

- Elindítható feladatok listája:

`todo list --startable`

- Új feladat hozzáadása a munkalistához:

`todo new {{thing_to_do}} --list {{work}}`

- Hely hozzáadása egy adott azonosítóval rendelkező feladathoz:

`todo edit --location {{location_name}} {{task_id}}`

- Egy feladat részleteinek megjelenítése:

`todo show {{task_id}}`

- Megadott azonosítóval rendelkező feladatok befejezettként való megjelölése:

`todo done {{task_id1 task_id2 ...}}`

- Feladat törlése:

`todo delete {{task_id}}`

- Elvégezett feladatok törlése és a megmaradt feladatok azonosítóinak visszaállítása:

`todo flush`
