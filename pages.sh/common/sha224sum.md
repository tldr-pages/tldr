# sha224sum

> Izračunava SHA224 kriptografske kontrolne brojeve.
> Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA224 kontrolni broj za datoteku:

`sha224sum {{datoteka1}}`

- Izračunaj SHA224 kontrolne brojeve za više datoteka:

`sha224sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA224 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha224sum -c {{datoteka.sha224}}`
