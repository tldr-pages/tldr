# ansible-galaxy

> Esegui varie operazioni inerenti ai Ruoli e alle Collezioni in Ansible.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Lista i ruoli o le collezioni installate:

`ansible-galaxy {{ruolo|collezione}} list`

- Cerca un ruolo con vari livelli di verbosità (`-v` deve essere specificato alla fine):

`ansible-galaxy role search {{keyword}} -v{{vvvvv}}`

- Installa o rimuovi ruoli:

`ansible-galaxy role {{install|remove}} {{nome_ruolo1 nome_ruolo2 ...}}`

- Crea un nuovo ruolo:

`ansible-galaxy role init {{nome_ruolo}}`

- Ottieni informazioni inerenti a un ruolo:

`ansible-galaxy role info {{nome_ruolo}}`

- Installa o rimuovi collezioni:

`ansible-galaxy collection {{install|remove}} {{nome_collezione1 nome_collezione2 ...}}`

- Mostra aiuto su ruoli o collezioni:

`ansible-galaxy {{ruolo|collezione}} {{[-h|--help]}}`
