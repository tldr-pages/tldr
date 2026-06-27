# cat

> Skriv ut og slå sammen filer.
> Mer informasjon: <https://manned.org/cat.1posix>.

- Skriv ut innholdet i en fil til `stdout`:

`cat {{sti/til/fil}}`

- Slå sammen flere filer til en utdatafil:

`cat {{sti/til/fil1 sti/til/fil2 ...}} > {{sti/til/utdatafil}}`

- Legg flere filer til på slutten av en utdatafil:

`cat {{sti/til/fil1 sti/til/fil2 ...}} >> {{sti/til/utdatafil}}`

- Kopier innholdet i en fil til en utdatafil uten bufring:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Skriv `stdin` til en fil:

`cat - > {{sti/til/fil}}`
