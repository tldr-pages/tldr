# pyenv

> Passa da una distribuzione all'altra di Python in modo semplice.
> Vedi anche: `asdf`.
> Maggiori informazioni: <https://manned.org/pyenv>.

- Elenca i comandi disponibili:

`pyenv commands`

- Elenca tutte le distribuzioni di Python presenti nella directory `${PYENV_ROOT}/versions`:

`pyenv versions`

- Elenca tutte le versioni di Python che possono essere installate da upstream:

`pyenv install --list`

- Installa una distribuzione di Python nella directory `${PYENV_ROOT}/versions`:

`pyenv install {{2.7.10}}`

- Disinstalla una distribuzione di Python dalla directory `${PYENV_ROOT}/versions`:

`pyenv uninstall {{2.7.10}}`

- Imposta la distribuzione di Python da utilizzare globalmente sulla macchina:

`pyenv global {{2.7.10}}`

- Imposta la distribuzione di Python da utilizzare nella directory corrente e in tutte le relative sottodirectory:

`pyenv local {{2.7.10}}`
