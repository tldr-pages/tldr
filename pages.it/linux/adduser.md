# adduser

> Servizio per aggiungere utenti.
> Maggiori informazioni: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Crea un nuovo utente con una directory home predefinita e richiede all'utente di impostare una password:

`adduser {{nome_utente}}`

- Crea un utente senza una directory home:

`adduser --no-create-home {{nome_utente}}`

- Crea un utente con una directory home nel percorso specificato:

`adduser --home {{percorso/della/home}} {{nome_utente}}`

- Crea un nuovo utente con l'interprete di comandi(shell) specificato come shell di accesso:

`adduser --shell {{percorso/della/shell}} {{nome_utente}}`

- Crea un nuovo utente appartenente al gruppo specificato:

`adduser --ingroup {{gruppo}} {{nome_utente}}`

- Aggiunge un utente esistente al gruppo specificato:

`adduser {{nome_utente}} {{gruppo}}`
