# icalBuddy

> Parancssori segédprogram a macOS naptáradatbázisából történő események és feladatok nyomtatásához. További információ: <https://hasseg.org/icalBuddy/>.

- A mai nap későbbi eseményeinek megjelenítése:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- Befejezetlen feladatok megjelenítése:

`icalBuddy uncompletedTasks`

- Formázott lista megjelenítése naptár szerint elválasztva a mai nap összes eseményéről:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- Megadott számú napra vonatkozó feladatok megjelenítése:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+{{days}}"`

- Események megjelenítése egy időtartományban:

`icalBuddy eventsFrom:{{start_date}} to:{{end_date}}`
