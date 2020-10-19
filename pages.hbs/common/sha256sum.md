# sha256sum

> Izračunava SHA256 kriptografske kontrolne brojeve.

- Izračunaj SHA256 kontrolni broj za datoteku:

`sha256sum {{datoteka1}}`

- Izračunaj SHA256 kontrolne brojeve za više datoteka:

`sha256sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA256 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha256sum -c {{datoteka.sha256}}`
