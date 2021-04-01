# sha512sum

> Izračunava SHA512 kriptografske kontrolne brojeve.
> Više informacija: <https://man.archlinux.org/man/sha512sum.1>.

- Izračunaj SHA512 kontrolni broj za datoteku:

`sha512sum {{datoteka1}}`

- Izračunaj SHA512 kontrolne brojeve za više datoteka:

`sha512sum {{datoteka1}} {{datoteka2}}`

- Pročitaj datoteku SHA512 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha512sum -c {{datoteka.sha512}}`
