# leave

> Állítson be emlékeztetőt, amikor el kell mennie. Az emlékeztetők eltávolításához használja a `kill $(pidof leave)` címet. További információ: <https://www.freebsd.org/cgi/man.cgi?query=leave>.

- Emlékeztető beállítása egy adott időpontra:

`leave {{time_to_leave}}`

- Állítson be emlékeztetőt a déli távozásra:

`leave {{1200}}`

- Állítson be emlékeztetőt egy adott időn belül:

`leave +{{amount_of_time}}`

- Állítson be emlékeztetőt, hogy 4 óra 4 perc múlva távozzon:

`leave +{{0404}}`
