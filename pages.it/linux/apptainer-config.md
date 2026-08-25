# apptainer config

> Gestisce varie configurazioni di Apptainer.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_config.html>.

- Aggiunge un mapping utente fakeroot:

`sudo apptainer config fakeroot {{[-a|--add]}} {{nome_utente}}`

- Rimuove un mapping utente fakeroot:

`sudo apptainer config fakeroot {{[-r|--remove]}} {{nome_utente}}`

- Abilita un mapping utente fakeroot:

`sudo apptainer config fakeroot {{[-e|--enable]}} {{nome_utente}}`

- Disabilita un mapping utente fakeroot:

`sudo apptainer config fakeroot {{[-d|--disable]}} {{nome_utente}}`

- Ottiene il valore corrente di una direttiva di configurazione globale:

`sudo apptainer config global {{[-g|--get]}} {{direttiva}}`

- Imposta il valore di una direttiva di configurazione globale:

`sudo apptainer config global {{[-s|--set]}} {{direttiva}} {{valore}}`

- Annulla il valore di una direttiva di configurazione globale:

`sudo apptainer config global {{[-u|--unset]}} {{direttiva}} {{valore}}`

- Reimposta una direttiva di configurazione globale al suo valore predefinito:

`sudo apptainer config global {{[-r|--reset]}} {{direttiva}}`
