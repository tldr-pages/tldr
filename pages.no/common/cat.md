# cat

> Skriv ut og sammenføy filer.
> Mer informasjon: <https://www.gnu.org/software/coreutils/cat>.

- Skriv ut innholdet i en fil til standard utgang:

`cat {{fil}}`

- Sammenføy flere filer til en målfil:

`cat {{fil1}} {{fil2}} > {{målfil}}`

- Legg til flere filer til målfilen:

`cat {{fil1}} {{fil2}} >> {{målfil}}`

- Nummerer alle utgangslinjer:

`cat -n {{fil}}`

- Vis tegn som ikke kan skrives ut og mellomrom (med `M-` prefiks hvis det ikke er ASCII-tegn):

`cat -v -t -e {{fil}}`
