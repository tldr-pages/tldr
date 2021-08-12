# hg pull

> Trageți modificările dintr-un depozit specificat în depozitul local.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#pull>

- Trageți din calea sursă „implicită”:

`hg pull`

- Trageți dintr-un depozit sursă specificat:

`hg pull {{path/to/source_repository}}`

- Actualizați depozitul local la capul telecomenzii:

`hg pull --update`

- Trageți modificările chiar și atunci când depozitul de la distanță nu are legătură:

`hg pull --force`

- Specificați un anumit set de modificări de revizuire pentru a trage în sus la:

`hg pull --rev {{revision}}`

- Specificați o ramură specifică pentru a trage:

`hg pull --branch {{branch}}`

- Specificați un anumit marcaj pentru a trage:

`hg pull --bookmark {{bookmark}}`
