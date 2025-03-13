# tail

> Prikazuje krajnji deo datoteke.
> Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Prikaži poslednjih 'broj' linija u datoteci:

`tail {{[-n|--lines]}} {{broj}} {{datoteka}}`

- Prikaži celu datoteku od linije 'broj':

`tail {{[-n|--lines]}} +{{broj}} {{datoteka}}`

- Prikaži poslednjih 'broj' bajtova u datoteci:

`tail {{[-c|--bytes]}} {{broj}} {{datoteka}}`

- Čitaj datoteku sve do `Ctrl + C`:

`tail {{[-f|--follow]}} {{datoteka}}`

- Čitaj datoteku sve do `Ctrl + C`, čak i kad je datoteka rotirana:

`tail {{[-F|--retry --follow]}} {{datoteka}}`
