# sha384sum

> Izračunava SHA384 kriptografske kontrolne brojeve.
> Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA384 kontrolni broj za datoteku:

`sha384sum {{datoteka1}}`

- Izračunaj SHA384 kontrolne brojeve za više datoteka:

`sha384sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA384 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha384sum -c {{datoteka.sha384}}`
