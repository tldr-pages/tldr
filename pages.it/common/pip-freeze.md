# pip freeze

> Elenca i pacchetti installati nel formato dei requisiti (requirements).
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_freeze/>.

- Elenca i pacchetti installati:

`pip freeze`

- Scrivi i pacchetti installati nel file `requirements.txt`:

`pip freeze > requirements.txt`

- Elenca i pacchetti installati in un ambiente virtuale, escludendo i pacchetti installati globalmente:

`pip freeze {{[-l|--local]}}`

- Elenca i pacchetti installati nel sito dell'utente (user-site):

`pip freeze --user`

- Elenca tutti i pacchetti, inclusi `pip`, `distribute`, `setuptools` e `wheel` (vengono saltati per impostazione predefinita):

`pip freeze --all`
