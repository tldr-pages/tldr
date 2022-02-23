# ac

> Imprimeix estadístiques sonre el temps de connexió dels usuaris.
> Més informació: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprimeix el temps de connexió del usuari actual en hores:

`ac`

- Imprimeix el temps total de connexió de tots els usuaris en hores:

`ac --individual-totals`

- Imprimeix el temps total de connexió d'un usuari concret en hores:

`ac --individual-totals {{nom_usuari}}`

- Imprimeix el temps de connexió d'un usuari concret en hores per dia (amb total):

`ac --daily-totals --individual-totals {{nom_usuari}}`

- Mostra també detalls adicionals:

`ac --compatibility`
