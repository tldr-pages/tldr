# CONFIG

> Wijzig of bevraag DOSBox-instellingen tijdens runtime; bewaar configs/talen.
> Meer informatie: <https://www.dosbox.com/wiki/CONFIG>.

- Schrijf de huidige configuratie naar een bestand (lokale schijf):

`CONFIG -writeconf {{pad/naar/bestand.conf}}`

- Schrijf de huidige taalstrings naar een bestand:

`CONFIG -writelang {{pad/naar/bestand.lang}}`

- Schakel de beveiligde modus in (schakelt MOUNT/IMGMOUNT/BOOT uit):

`CONFIG -securemode`

- Stel een eigenschap in (bijv. CPU-cycli):

`CONFIG -set "cpu cycles={{10000}}"`

- Stel een eigenschap in (bijv. EMS uitschakelen):

`CONFIG -set "dos ems=off"`

- Haal de waarde van een eigenschap op (opgeslagen in `%CONFIG%`):

`CONFIG -get "cpu core"`
