# pip config

> Gestisci la configurazione locale e globale per pip.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_config/>.

- Elenca tutti i valori di configurazione:

`pip config list`

- Mostra i file di configurazione e i loro valori:

`pip config debug`

- Imposta il valore per un'opzione di comando:

`pip config set {{command.option}} {{valore}} {{--global|--user|--site}}`

- Ottieni il valore per un'opzione di comando:

`pip config get {{command.option}} {{--global|--user|--site}}`

- Rimuovi il valore impostato per un'opzione di comando:

`pip config unset {{command.option}} {{--global|--user|--site}}`

- Modifica il file di configurazione con l'editor predefinito:

`pip config edit {{--global|--user|--site}}`

- Modifica il file di configurazione con uno specifico editor:

`pip config edit {{--global|--user|--site}} --editor {{percorso/del/binario_editor}}`
