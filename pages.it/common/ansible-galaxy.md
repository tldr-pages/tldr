# ansible-galaxy

> Esegui varie operazioni inerenti i Ruoli e le Collezioni in Ansible.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Lista delle installazioni sia dei ruoli che delle collezioni:

`ansible-galaxy {{role|collection}} list`

- Avvia la ricerca per un ruolo con vari livelli di definizione (verbosità)  (`-v` dovrebbe essere specificato alla fine):

`ansible-galaxy role search {{keyword}} -v{{vvvvv}}`

- Installa o rimuove ruoli:

`ansible-galaxy role {{install|remove}} {{role_name1 role_name2 ...}}`

- Crea un nuovo ruolo:

`ansible-galaxy role init {{role_name}}`

- Ottiene informazioni inerenti un ruolo:

`ansible-galaxy role info {{role_name}}`

- Installa o rimuove installazioni:

`ansible-galaxy collection {{install|remove}} {{collection_name1 collection_name2 ...}}`

- Mostra supporto circa i ruoli e le collezioni:

`ansible-galaxy {{role|collection}} {{-h|--help}}`
