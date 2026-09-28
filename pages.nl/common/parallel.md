# parallel

> Voer commando's uit op meerdere CPU-kernen.
> Zie ook: `xargs`.
> Meer informatie: <https://www.gnu.org/software/parallel/man.html>.

- Gzip meerdere bestanden tegelijk, met gebruik van alle kernen:

`parallel gzip ::: {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Lees argumenten van `stdin`, voer 4 taken tegelijk uit:

`ls *.txt | parallel {{[-j|--jobs]}} 4 gzip`

- Converteer JPEG-afbeeldingen naar PNG met behulp van vervangingsstrings:

`parallel convert {} {.}.png ::: *.jpg`

- Parallel xargs, stop zoveel mogelijk argumenten in één commando:

`{{argumenten}} | parallel -X {{commando}}`

- Verdeel `stdin` in blokken van ~1M, geef elk blok door aan `stdin` van een nieuw commando:

`cat {{groot_bestand.txt}} | parallel --pipe --block 1M {{commando}}`

- Voer uit op meerdere machines via SSH:

`parallel {{[-S|--sshlogin]}} {{machine1}},{{machine2}} {{commando}} ::: {{arg1}} {{arg2}}`

- Download 4 bestanden tegelijk vanuit een tekstbestand met links, met voortgangsweergave:

`parallel {{[-j|--jobs]}} 4 --bar --eta curl {{[-sO|--silent --remote-name]}} {} :::: {{pad/naar/links.txt}}`

- Toon de taken die `parallel` uitvoert in `stderr`:

`parallel {{[-t|--verbose]}} {{commando}} ::: {{argumenten}}`
