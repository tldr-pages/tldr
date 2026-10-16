# getArch.py

> Bepaal de OS-architectuur (x86 of x64) van een remote Windows-systeem.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Controleer de architectuur van een enkel doelsysteem:

`getArch.py -target {{doel}}`

- Controleer de architectuur van meerdere doelen van een bestand (één per regel):

`getArch.py -targets {{pad/naar/doelen_bestand}}`

- Stel een custom socket timeout in (standaard is 2 seconden):

`getArch.py -target {{doel}} -timeout {{seconden}}`

- Schakel debug-modus in voor gedetailleerde uitvoer:

`getArch.py -target {{doel}} -debug`
