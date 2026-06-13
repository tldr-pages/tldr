# deluser

> Elimina un utente dal sistema.
> Maggiori informazioni: <https://manned.org/deluser>.

- Rimuove un utente:

`sudo deluser {{nome_utente}}`

- Rimuove un utente e la sua directory home:

`sudo deluser --remove-home {{nome_utente}}`

- Rimuove un utente e la sua home, ma salva i file in un `.tar.gz` nella directory specificata:

`sudo deluser --backup-to {{percorso/alla/directory_di_backup}} --remove-home {{nome_utente}}`

- Rimuove un utente e tutti i file di sua proprietà:

`sudo deluser --remove-all-files {{nome_utente}}`
