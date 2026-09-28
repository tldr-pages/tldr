# restorecon

> Herstel de SELinux-beveiligingscontext op bestanden/mappen volgens persistente regels.
> Zie ook: `semanage fcontext`.
> Meer informatie: <https://manned.org/restorecon>.

- Toon de huidige beveiligingscontext van een bestand of map:

`ls {{[-dlZ|--directory -l --context]}} {{pad/naar/bestand_of_map}}`

- Herstel de beveiligingscontext van een bestand of map:

`restorecon {{pad/naar/bestand_of_map}}`

- Herstel de beveiligingscontext van een map recursief en toon alle gewijzigde labels:

`restorecon -R -v {{pad/naar/map}}`

- Herstel de beveiligingscontext van een map recursief, met gebruik van alle beschikbare threads, en toon voortgang:

`restorecon -R -T {{0}} -p {{pad/naar/map}}`

- Bekijk vooraf welke labelwijzigingen zouden plaatsvinden zonder ze toe te passen:

`restorecon -R -n -v {{pad/naar/map}}`
