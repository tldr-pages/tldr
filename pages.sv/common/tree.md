# tree

> Visa innehållet i den nuvarande katalogen som ett träd.
> Mer information: <https://manned.org/tree>.

- Visa filer och katalogen upp till `num` nivåer djupt (där 1 är den nuvarande katalogen):

`tree -L {{num}}`

- Visa endast kataloger:

`tree -d`

- Visa även dolda filer med färgläggning på:

`tree -a -C`

- Visa trädstrukturen utan indenteringslinjer, med den fullständiga sökvägen till filen istället (använd `-N` för att inte maskera icke-utskrivbara tecken):

`tree -i -f`

- Visa storleken för varje fil samt den sammanlagda storleken för varje katalog, i ett lättläst format:

`tree -s -h --du`

- Visa filer i trädstrukturen som matchar ett jokerteckenmönster (glob), och uteslut kataloger som inte innehåller några matchande filer:

`tree -P '{{*.txt}}' --prune`

- Visa kataloger i trädstrukturen som matchar ett jokerteckenmönster (glob), och uteslut kataloger som inte ligger i sökvägen till den önskade katalogen:

`tree -P {{katalog_namn}} --matchdirs --prune`

- Visa trädstrukturen utan de angivna katalogerna:

`tree -I '{{katalog_namn1|katalog_namn2}}'`
