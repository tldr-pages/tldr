# sha1sum

> Izračunava SHA1 kriptografske kontrolne brojeve.

- Izračunaj SHA1 kontrolni broj za datoteku:

`sha1sum {{datoteka1}}`

- Izračunaj SHA1 kontrolne brojeve za više datoteka:

`sha1sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA1 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha1sum -c {{datoteka.sha1}}`
