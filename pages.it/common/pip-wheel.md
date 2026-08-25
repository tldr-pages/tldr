# pip wheel

> Crea archivi wheel per pacchetti e dipendenze.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_wheel/>.

- Crea un file wheel per un pacchetto:

`pip wheel {{pacchetto}}`

- Crea file wheel per i pacchetti in un file dei requisiti (requirements):

`pip wheel {{[-r|--requirement]}} {{percorso/del/requirements.txt}}`

- Crea un file wheel in una directory specifica:

`pip wheel {{pacchetto}} {{[-w|--wheel-dir]}} {{percorso/della/directory}}`

- Crea un file wheel senza dipendenze:

`pip wheel {{pacchetto}} --no-deps`

- Crea un file wheel da un progetto locale:

`pip wheel {{percorso/del/progetto}}`

- Crea un file wheel da un repository Git:

`pip wheel git+{{https://github.com/nome_utente/repository.git}}`
