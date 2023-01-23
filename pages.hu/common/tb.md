# tb

> CLI a feladatok és jegyzetek kezelésére több táblán keresztül. További információ: <https://github.com/klaussinani/taskbook>.

- Új feladat hozzáadása egy táblához:

`tb --task {{task_description}} @{{board_name}}`

- Új jegyzet hozzáadása egy táblához:

`tb --note {{note_description}} @{{board_name}}`

- A tétel prioritásának szerkesztése:

`tb --priority @{{item_id}} {{priority}}`

- A tétel bejelölése/elhagyása:

`tb --check {{item_id}}`

- Az összes ellenőrzött elem archiválása:

`tb --clear`

- Elem áthelyezése egy táblára:

`tb --move @{{item_id}} {{board_name}}`
