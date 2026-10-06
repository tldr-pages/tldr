# code

> Cross-platform en uitbreidbare code-editor.
> Meer informatie: <https://code.visualstudio.com/docs/configure/command-line>.

- Start Visual Studio Code:

`code`

- Open specifieke bestanden/mappen:

`code {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Vergelijk twee specifieke bestanden:

`code {{[-d|--diff]}} {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Open specifieke bestanden/mappen in een nieuw venster:

`code {{[-n|--new-window]}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Installeer/verwijder een specifieke extensie:

`code --{{install|uninstall}}-extension {{uitgever.extensie}}`

- Toon diagnostische en procesinformatie over het actieve code-venster:

`code {{[-s|--status]}}`

- Print geïnstalleerde extensies met hun versies:

`code --list-extensions --show-versions`

- Start de editor als superuser (root) en sla gebruikersgegevens op in een specifieke map:

`sudo code --user-data-dir {{pad/naar/map}}`
