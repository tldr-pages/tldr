# pip

> Gestore di pacchetti per Python.
> Alcuni sottocomandi come `install` hanno la propria documentazione d'uso.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip/>.

- Installa un pacchetto (vedi `pip install` per altri esempi di installazione):

`pip install {{pacchetto}}`

- Installa un pacchetto nella directory dell'utente invece della posizione predefinita di sistema:

`pip install --user {{pacchetto}}`

- Aggiorna un pacchetto:

`pip install {{[-U|--upgrade]}} {{pacchetto}}`

- Disinstalla un pacchetto:

`pip uninstall {{pacchetto}}`

- Salva i pacchetti installati in un file:

`pip freeze > {{requirements.txt}}`

- Elenca i pacchetti installati:

`pip list`

- Mostra informazioni su un pacchetto installato:

`pip show {{pacchetto}}`

- Installa pacchetti da un file:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
