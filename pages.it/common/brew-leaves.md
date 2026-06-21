# brew leaves

> Elenca le formule installate che non sono dipendenze di un'altra formula o cask installata.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#leaves---installed-on-request---installed-as-dependency>.

- Elenca le formule installate che non dipendono da altre formule o cask installate:

`brew leaves`

- Elenca solo le leaves installate manualmente:

`brew leaves {{[-r|--installed-on-request]}}`

- Elenca solo le leaves installate come dipendenze:

`brew leaves {{[-p|--installed-as-dependency]}}`

- Mostra l'aiuto:

`brew leaves {{[-h|--help]}}`
