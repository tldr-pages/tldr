# rsync

> Draag bestanden over naar of van een externe host (maar niet tussen twee externe hosts), met als standaard via SSH.
> Om een pad te specificeren, gebruik `gebruiker@host:pad/naar/bestand_of_map`.
> Meer informatie: <https://download.samba.org/pub/rsync/rsync.1>.

- Draag een bestand over:

`rsync {{pad/naar/bron}} {{pad/naar/bestemming}}`

- Gebruik archiefmodus (kopieer recursief mappen, kopieer symlinks zonder ze op te lossen en behoud machtigingen, eigendom en wijzigingstijden):

`rsync {{[-a|--archive]}} {{pad/naar/bron}} {{pad/naar/bestemming}}`

- Comprimeer de data wanneer deze worden verzonden naar de bestemming, toon verbose en voor mensen leesbare voortgang, en behoud gedeeltelijk overgedragen bestanden als er een onderbreking is:

`rsync {{[-zvhP|--compress --verbose --human-readable --partial --progress]}} {{pad/naar/bron}} {{pad/naar/bestemming}}`

- Kopieer recursief mappen:

`rsync {{[-r|--recursive]}} {{pad/naar/bron}} {{pad/naar/bestemming}}`

- Draag de inhoud van een map over, maar niet de map zelf:

`rsync {{[-r|--recursive]}} {{pad/naar/bron/}} {{pad/naar/bestemming}}`

- Gebruik archiefmodus, los symlinks op en sla bestanden over die nieuwer zijn op de bestemming:

`rsync {{[-auL|--archive --update --copy-links]}} {{pad/naar/bron}} {{pad/naar/bestemming}}`

- Draag een map over van een externe host waarop `rsyncd` draait en verwijder bestanden op de bestemming die niet op de bron bestaan:

`rsync {{[-r|--recursive]}} --delete rsync://{{host}}:{{pad/naar/bron}} {{pad/naar/bestemming}}`

- Draag een bestand over via SSH met een andere poort dan de standaardpoort (22) en toon globale voortgang:

`rsync {{[-e|--rsh]}} 'ssh -p {{poort}}' --info=progress2 {{host}}:{{pad/naar/bron}} {{pad/naar/bestemming}}`
