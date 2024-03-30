# ansible-galaxy

> Crea e gestisci ruoli di Ansible.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Installa un ruolo:

`ansible-galaxy install {{nome_utente}}.{{ruolo}}`

- Rimuovi un ruolo:

`ansible-galaxy remove {{nome_utente}}.{{ruolo}}`

- Elenca i ruoli installati:

`ansible-galaxy list`

- Cerca un determinato ruolo:

`ansible-galaxy search {{nome_ruolo}}`

- Crea un nuovo ruolo:

`ansible-galaxy init {{nome_ruolo}}`

- Acquisisci informazioni su un ruolo di un utente:

`ansible-galaxy role info {{nome_utente}}.{{nome_ruolo}}`

- Acquisisci informazioni su una collection:

`ansible-galaxy collection info {{nome_utente}}.{{nome_raccolta}}`
