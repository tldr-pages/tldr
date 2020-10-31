# adduser

> Servizio per aggiungere utenti.

- Crea un nuovo utente con una home directory predefinita e richiede all'utente di impostare una password:

`adduser {{nome_utente}}`

- Crea un utente senza una home directory:

`adduser --no-create-home {{nome_utente}}`

- Crea un utente con una home directory nel percorso specificato:

`adduser --home {{percorso/all/home}} {{nome_utente}}`

- Crea un nuovo utente con l'interprete di comandi(shell) specificato come shell di accesso:

`adduser --shell {{percorso/alla/shell}} {{nome_utente}}`

- Crea un nuovo utente appartenente al gruppo specificato:

`adduser --ingroup {{gruppo}} {{nome_utente}}`

- Aggiunge un utente esistente al gruppo specificato:

`adduser {{nome_utente}} {{gruppo}}`
