# pip list

> Elenca i pacchetti Python installati.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_list/>.

- Elenca i pacchetti installati:

`pip list`

- Elenca i pacchetti obsoleti che possono essere aggiornati:

`pip list {{[-o|--outdated]}}`

- Elenca i pacchetti aggiornati:

`pip list {{[-u|--uptodate]}}`

- Elenca i pacchetti con formattazione JSON:

`pip list --format json`

- Elenca i pacchetti che non sono richiesti da altri pacchetti:

`pip list --not-required`

- Elenca i pacchetti installati solo nel sito dell'utente (user-site):

`pip list --user`

- Elenca i pacchetti ed escludi i pacchetti modificabili (editable) dall'output:

`pip list --exclude-editable`

- Elenca i pacchetti nel formato freeze (a differenza di `pip freeze`, non mostra le informazioni sull'installazione modificabile):

`pip list --format freeze`
