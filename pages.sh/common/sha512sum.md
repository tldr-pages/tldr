# sha512sum

> Izračunava SHA512 kriptografske kontrolne brojeve.
> Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA512 kontrolni broj za datoteku:

`sha512sum {{datoteka1}}`

- Izračunaj SHA512 kontrolne brojeve za više datoteka:

`sha512sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA512 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha512sum -c {{datoteka.sha512}}`
