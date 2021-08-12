# gitsome

> O interfață bazată pe terminal pentru GitHub, accesată prin comanda `gh`.
> De asemenea, oferă sugestii de completare automată a meniurilor pentru comenzile `git`.
> Mai multe informaţii: <https://github.com/donnemartin/gitsome>

- Introduceți shell-ul gitsome (opțional), pentru a permite autocompletare și ajutor interactiv pentru Git (și gh) comenzi:

`gitsome`

- Configurarea integrării GitHub cu contul curent:

`gh configure`

- Lista notificărilor pentru contul curent (așa cum se vede în https://github.com/notifications):

`gh notifications`

- Listează repo-urile cu stele ale contului curent, filtrate de un șir de căutare dat:

`gh starred "{{python 3}}"`

- Vizualizați fluxul de activitate recent al unui depozit GitHub dat:

`gh feed {{tldr-pages/tldr}}`

- Vizualizați fluxul de activitate recent pentru un anumit utilizator GitHub, utilizând pagerul implicit (de exemplu, „mai puțin”):

`gh feed {{torvalds}} -p`
