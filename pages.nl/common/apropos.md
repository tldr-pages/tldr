# apropos

> Zoek in de handleiding-pagina's naar namen en beschrijvingen.
> Zie ook: `man`.
> Meer informatie: <https://manned.org/apropos>.

- Zoek naar een trefwoord met behulp van een `regex`:

`apropos {{regex}}`

- Zoek zonder de uitvoer te beperken tot de breedte van de terminal (lange uitvoer):

`apropos {{[-l|--long]}} {{regex}}`

- Zoek naar pagina's die overeenkomen met alle opgegeven `regex`:

`apropos {{regex_1}} {{[-a|--and]}} {{regex_2}} {{[-a|--and]}} {{regex_3}}`
