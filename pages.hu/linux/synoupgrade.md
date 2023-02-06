# synoupgrade

> A Synology DiskStation Manager (DSM) frissítése a parancssorból. További információ: <https://www.synology.com/dsm>.

- Ellenőrizze, hogy elérhetőek-e frissítések:

`sudo synoupgrade --check`

- A DSM verziójának frissítése nélkül ellenőrizheti a javítások meglétét:

`sudo synoupgrade --check-smallupdate`

- Töltse le a legújabb elérhető frissítést (használja a `--download-smallupdate` címet a javításokhoz):

`sudo synoupgrade --download`

- Indítsa el a frissítési folyamatot:

`sudo synoupgrade --start`

- Automatikus frissítés a legújabb verzióra:

`sudo synoupgrade --auto`

- Foltok alkalmazása a DSM verzió automatikus frissítése nélkül:

`sudo synoupgrade --auto-smallupdate`

- A DSM frissítése egy javítási fájl segítségével (abszolút elérési útvonalnak kell lennie):

`sudo synoupgrade --patch {{/path/to/file.pat}}`

- Súgó megjelenítése:

`synoupgrade`
