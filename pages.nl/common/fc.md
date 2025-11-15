# fc

> Open het meest recente commando voor bewerking en voer het uit.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-fc>.

- Open het laatste commando in de standaard systeemeditor en voer het uit na het aanpassen:

`fc`

- Specificeer een editor om mee te openen:

`fc -e '{{emacs}}'`

- Toon recente commando's uit de geschiedenis:

`fc -l`

- Toon recente commando's in omgekeerde volgorde:

`fc -l -r`

- Pas een commando uit de geschiedenis aan en voer het uit:

`fc {{nummer}}`

- Pas commando's in een gegeven interval aan en voer ze uit:

`fc '{{416}}' '{{420}}'`

- Toon de help:

`fc --help`
