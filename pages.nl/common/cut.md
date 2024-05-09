# cut

> Snij velden eruit vanuit `stdin` of bestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/cut>.

- Toon een specifiek karakter/veldbereik voor iedere regel:

`{{commando}} | cut --{{characters|fields}} {{1|1,10|1-10|1-|-10}}`

- Toon een bereik voor iedere regel met een specifieke scheiding:

`{{commando}} | cut --delimiter "{{,}}" --fields {{1}}`

- Toon een bereik van iedere regel voor een specifiek bestand:

`cut --characters {{1}} {{pad/naar/bestand}}`

- Toon specifieke velden van `NUL` afgesloten regels (bijv. zoals in `find . -print0`) in plaats van nieuwe regels:

`{{command}} | cut --zero-terminated --fields {{1}}`
