# reg flags

> Megjelenítheti vagy beállíthatja a beállításjegyeket a beállításkulcsokon. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-flags>.

- Egy adott kulcs aktuális zászlóinak megjelenítése:

`reg flags {{key_name}} query`

- A súgó és az elérhető zászlótípusok megjelenítése:

`reg flags /?`

- Megadott, szóközzel elválasztott zászlók beállítása és a nem említett zászlók beállításának megszüntetése egy adott kulcshoz:

`reg flags {{key_name}} set {{flag_names}}`

- Meghatározott zászlók beállítása egy adott kulcshoz és annak alkulcsaihoz:

`reg flags {{key_name}} set {{flag_names}} /s`
