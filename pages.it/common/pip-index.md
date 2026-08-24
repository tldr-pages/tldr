# pip index

> Ispeziona le informazioni disponibili dagli indici dei pacchetti.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_index/>.

- Elenca tutte le versioni disponibili di un pacchetto:

`pip index versions {{pacchetto}}`

- Elenca le versioni da un indice specifico:

`pip index versions {{pacchetto}} --index-url {{https://test.pypi.org/simple/}}`

- Includi le versioni pre-rilascio:

`pip index versions {{pacchetto}} --pre`

- Includi un indice aggiuntivo:

`pip index versions {{pacchetto}} --extra-index-url {{https://example.com/simple/}}`

- Elenca le versioni per una specifica piattaforma:

`pip index versions {{pacchetto}} --platform {{linux_x86_64}}`
