# dirname

> Berekent de bovenliggende map van een bestand of map.
> Meer informatie: <https://www.gnu.org/software/coreutils/dirname>.

- Bereken de bovenliggende map van een opgegeven pad:

`dirname {{pad/naar/bestand_of_map}}`

- Bereken de bovenliggende map van meerdere paden:

`dirname {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Scheid de uitvoer met een NUL-teken in plaats van een nieuwe regel (handig bij gebruik met `xargs`):

`dirname --zero {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`
