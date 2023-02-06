# query

> Megjeleníti a felhasználói munkamenetekre és folyamatokra vonatkozó információkat. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- Az összes felhasználói munkamenet megjelenítése:

`query session`

- A távoli számítógép aktuális felhasználói munkameneteinek megjelenítése:

`query session /server:{{hostname}}`

- Bejelentkezett felhasználók megjelenítése:

`query user`

- Az összes felhasználói munkamenet megjelenítése egy távoli számítógépen:

`query session /server:{{hostname}}`

- Az összes futó folyamat megjelenítése:

`query process`

- Folyamatok megjelenítése munkamenet vagy felhasználónév szerint:

`query process {{session_name|user_name}}`
