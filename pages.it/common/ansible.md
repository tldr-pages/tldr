# ansible

> Gestisci gruppi di computer da remoto via SSH.
> Usa il file `/etc/ansible/hosts` per aggiungere nuovi gruppi/host.
> Maggiori informazioni: <https://www.ansible.com/>.

- Lista gli host appartenenti ad un gruppo:

`ansible {{gruppo}} --list-hosts`

- Invia un ping ad un gruppo di host invocando il modulo "ping":

`ansible {{gruppo}} -m ping`

- Mostra informazioni su di un gruppo di host invocando il modulo "setup":

`ansible {{gruppo}} -m setup`

- Esegui un comando su un gruppo di host invocando il modulo "command" con degli argomenti:

`ansible {{gruppo}} -m command -a '{{comando_da_eseguire}}'`

- Esegui un comando con privilegi di amministratore:

`ansible {{gruppo}} --become --ask-become-pass -m command -a '{{comando}}'`

- Esegui un comando usando un file di inventory personalizzato:

`ansible {{gruppo}} -i {{file_inventory}} -m command -a '{{comando}}'`
