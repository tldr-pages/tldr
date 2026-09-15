# pip lock

> Blocca i pacchetti Python e le loro dipendenze in un file riproducibile.
> Funzionalità sperimentale di `pip`.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_lock/>.

- Genera un file `pylock.toml` per il progetto corrente:

`pip lock {{[-e|--editable]}} .`

- Blocca le dipendenze da un file dei requisiti (requirements):

`pip lock {{[-r|--requirement]}} {{percorso/del/requirements.txt}}`

- Specifica un file di output personalizzato per il blocco:

`pip lock {{[-o|--output]}} {{percorso/del/lockfile.toml}}`

- Blocca uno specifico pacchetto e le sue dipendenze:

`pip lock {{pacchetto}}`
