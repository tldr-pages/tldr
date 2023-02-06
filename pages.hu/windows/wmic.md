# wmic

> Interaktív shell a futó folyamatokról szóló részletes információkért. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- Alapvető nyelvtan:

`wmic {{alias}} {{where_clause}} {{verb_clause}}`

- Rövid részletek megjelenítése az éppen futó folyamatokról:

`wmic process list brief`

- Teljes részletek megjelenítése az éppen futó folyamatokról:

`wmic process list full`

- Hozzáférés bizonyos mezőkhöz, mint például a folyamat neve, a folyamat azonosítója és a szülői folyamat azonosítója:

`wmic process get {{name,processid,parentprocessid}}`

- Egy adott folyamatra vonatkozó információk megjelenítése:

`wmic process where {{name="example.exe"}} list full`

- Egy adott folyamat meghatározott mezőinek megjelenítése:

`wmic process where processid={{pid}} get {{name,commandline}}`

- Folyamat megállítása:

`wmic process {{pid}} delete`
