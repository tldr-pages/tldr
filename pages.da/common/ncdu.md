# ncdu

> Diskbrugsanalysator med en ncurses-grænseflade.
> Mere information: <https://manned.org/ncdu>.

- Analysér den nuværende arbejdsmappe:

`ncdu`

- Definér farvevalg for output:

`ncdu --color {{dark|off}}`

- Analysér en given mappe:

`ncdu {{sti/til/mappe}}`

- Gem resultater til en fil:

`ncdu -o {{sti/til/fil}}`

- Ekskludér filer der matcher et mønster. Argumentet kan gives flere gange for at tilføje flere mønstre:

`ncdu --exclude '{{*.txt}}'`
