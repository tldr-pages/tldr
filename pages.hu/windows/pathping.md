# pathping

> A `ping` és a `tracert` jellemzőit ötvöző nyomkövető eszköz. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>.

- Pingeljen és kövesse nyomon az útvonalat egy állomáshoz:

`pathping {{hostname}}`

- Ne végezzen fordított keresést az IP-címről a gazdanévre:

`pathping {{hostname}} -n`

- Adja meg a célpont keresésének maximális ugrásszámát (az alapértelmezett 30):

`pathping {{hostname}} -h {{max_hops}}`

- Adja meg a pingelések közötti várakozási idő milliszekundumát (az alapértelmezett 240):

`pathping {{hostname}} -p {{time}}`

- Megadja a lekérdezések számát ugrásonként (az alapértelmezett érték 100):

`pathping {{hostname}} -q {{queries}}`

- IPV4 használatának kikényszerítése:

`pathping {{hostname}} -4`

- IPV6 használat kikényszerítése:

`pathping {{hostname}} -6`

- Részletes használati információk megjelenítése:

`pathping /?`
