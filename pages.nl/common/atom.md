# atom

> Een platformonafhankelijke inplugbare tekstbewerker.
> Plugins zijn beheerd door `apm`.
> Opmerking: Atom is niet meer actief en wordt niet meer actief onderhouden. Gebruik in plaats hiervan `zed`.
> Meer informatie: <https://atom.io/>.

- Open een bestand of map:

`atom {{pad/naar/bestand_of_map}}`

- Open een bestand of map in een nieuw venster:

`atom {{[-n|--new-window]}} {{pad/naar/bestand_of_map}}`

- Open een bestand of map in een bestaand venster:

`atom {{[-a|--add]}} {{pad/naar/bestand_of_map}}`

- Open Atom in veilige modus (laadt geen geïnstalleerde pakketten):

`atom --safe`

- Voorkom dat Atom zich vertakt in de achtergrond, en houdt Atom in de terminal:

`atom {{[-f|--foreground]}}`

- Wacht op het Atom venster om zich te sluiten voor door te gaan (handig voor Git commit bewerker):

`atom {{[-w|--wait]}}`
