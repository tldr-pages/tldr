# sha1sum

> Izračunava SHA1 kriptografske kontrolne brojeve.
> Više informacija: <https://www.gnu.org/software/coreutils/sha1sum>.

- Izračunaj SHA1 kontrolni broj za datoteku:

`sha1sum {{datoteka1}}`

- Izračunaj SHA1 kontrolne brojeve za više datoteka:

`sha1sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA1 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha1sum -c {{datoteka.sha1}}`
