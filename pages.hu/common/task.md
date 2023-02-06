# task

> Parancssori feladatlista-kezelő. További információ: <https://taskwarrior.org/docs/>.

- Új, holnap esedékes feladat hozzáadása:

`task add {{description}} due:{{tomorrow}}`

- Egy feladat prioritásának frissítése:

`task {{task_id}} modify priority:{{H|M|L}}`

- Egy feladat befejezése:

`task {{task_id}} done`

- Feladat törlése:

`task {{task_id}} delete`

- Az összes nyitott feladat listázása:

`task list`

- A hét vége előtt esedékes nyitott feladatok listázása:

`task list due.before:{{eow}}`

- Grafikus leégési diagram megjelenítése napok szerint:

`task burndown.daily`

- Az összes jelentés listázása:

`task reports`
