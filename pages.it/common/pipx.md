# pipx

> Installa ed esegui applicazioni Python in ambienti isolati.
> Maggiori informazioni: <https://manned.org/pipx>.

- Esegui un'applicazione in un ambiente virtuale temporaneo:

`pipx run {{pycowsay}} {{moo}}`

- Installa un pacchetto in un ambiente virtuale e aggiungi i suoi punti di ingresso al path:

`pipx install {{pacchetto}}`

- Disinstalla un pacchetto:

`pipx uninstall {{pacchetto}}`

- Elenca i pacchetti installati:

`pipx list`

- Esegui un'applicazione in un ambiente virtuale temporaneo con un nome di pacchetto diverso dall'eseguibile:

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`

- Inietta dipendenze in un ambiente virtuale esistente:

`pipx inject {{pacchetto}} {{dipendenza1 dipendenza2 ...}}`

- Installa un pacchetto in un ambiente virtuale con argomenti pip:

`pipx install --pip-args='{{argomenti_pip}}' {{pacchetto}}`

- Aggiorna, reinstalla o disinstalla tutti i pacchetti installati:

`pipx {{upgrade-all|uninstall-all|reinstall-all}}`
