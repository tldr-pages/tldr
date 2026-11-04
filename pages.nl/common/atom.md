# atom

> Een platformonafhankelijke inplugbare tekstbewerker.
> Plugins worden beheerd door `apm`.
> Opmerking: Atom is niet meer in ontwikkeling en wordt niet meer actief onderhouden. Gebruik in plaats hiervan `zed`.
> Meer informatie: <https://atom.io/>.

- Open een bestand of map:

`atom {{pad/naar/bestand_of_map}}`

- Open een bestand of map in een nieuw venster:

`atom {{[-n|--new-window]}} {{pad/naar/bestand_of_map}}`

- Open een bestand of map in een bestaand venster:

`atom {{[-a|--add]}} {{pad/naar/bestand_of_map}}`

- Open Atom in veilige modus (laadt geen extra pakketten):

`atom --safe`

- Voorkom dat Atom zich vertakt in de achtergrond, en houd Atom in de terminal:

`atom {{[-f|--foreground]}}`

- Wacht totdat het Atom-venster gesloten wordt voordat er wordt doorgegaan (handig voor de Git commit-editor):

`atom {{[-w|--wait]}}`
