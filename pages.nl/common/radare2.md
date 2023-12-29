# radare2

> Een set van reverse engineering tools.
> Meer informatie: <https://www.radare.org/r/docs.html>.

- Open een schrijfbaar bestand zonder het parsen van de bestandsformaat headers:

`radare2 -nw {{pad/naar/binary}}`

- Debug een programma:

`radare2 -d {{pad/naar/binary}}`

- Voer een script uit voordat de interactieve CLI start:

`radare2 -i {{pad/naar/script.r2}} {{pad/naar/binary}}`

- Toon help tekst voor ieder commando in de interactieve CLI:

`> {{radare2_commando}}?`

- Voer een shell commando uit vanuit de interactieve CLI:

`> !{{shell_commando}}`

- Dump raw bytes van het huidige block naar een bestand:

`> pr > {{pad/naar/bestand.bin}}`
