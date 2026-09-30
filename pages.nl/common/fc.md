# fc

> Open de recente commando's voor bewerking en voer ze vervolgens uit.
> Zie ook: `history`.
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

- Voer het vorige commando onmiddellijk uit zonder een editor te openen en vervang alle voorkomens van een string door een andere string:

`fc -s {{string1}}={{string2}}`

- Toon de help:

`fc --help`
