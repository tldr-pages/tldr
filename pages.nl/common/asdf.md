# asdf

> Beheer versies van verschillende pakketten.
> Meer informatie: <https://asdf-vm.com/manage/commands.html>.

- Toon alle beschikbare plug-ins:

`asdf plugin list all`

- Installeer een plugin:

`asdf plugin add {{naam}}`

- Toon alle beschikbare versies voor een pakket:

`asdf list all {{naam}}`

- Installeer een specifieke versie van een pakket:

`asdf install {{naam}} {{versie}}`

- Stel de globale versie voor een pakket in:

`asdf set -u {{naam}} {{versie}}`

- Stel de lokale versie voor een pakket in:

`asdf set {{naam}} {{versie}}`

- Bekijk de huidige versie die voor een pakket wordt gebruikt:

`asdf current {{naam}}`
