# tail

> Prikazuje krajnji deo datoteke.

- Prikaži poslednjih 'broj' linija u datoteci:

`tail -n {{broj}} {{datoteka}}`

- Prikaži celu datoteku od linije 'broj':

`tail -n +{{broj}} {{datoteka}}`

- Prikaži poslednjih 'broj' bajtova u datoteci:

`tail -c {{broj}} {{datoteka}}`

- Čitaj datoteku sve do `Ctrl + C`:

`tail -f {{datoteka}}`

- Čitaj datoteku sve do `Ctrl + C`, čak i kad je datoteka rotirana:

`tail -F {{datoteka}}`
