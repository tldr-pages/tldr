# ansible

> Gestisce gruppi di computer da remoto via SSH.
> Usa il file `/etc/ansible/hosts` per aggiungere nuovi gruppi/host.
> Alcuni comandi aggiuntivi, come `galaxy`, hanno la propria documentazione.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Elenca gli host appartenenti ad un gruppo:

`ansible {{gruppo}} --list-hosts`

- Invia un ping ad un gruppo di host invocando il modulo "ping":

`ansible {{gruppo}} {{[-m|--module-name]}} ping`

- Mostra informazioni su un gruppo di host invocando il modulo "setup":

`ansible {{gruppo}} {{[-m|--module-name]}} setup`

- Esegui un comando su un gruppo di host invocando il modulo "command" con degli argomenti:

`ansible {{gruppo}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{comando_da_eseguire}}'`

- Esegui un comando con privilegi di amministratore:

`ansible {{gruppo}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{comando}}'`

- Esegui un comando usando un file di inventory personalizzato:

`ansible {{gruppo}} {{[-i|--inventory]}} {{file_inventory}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{comando}}'`

- Elenca i gruppi in un inventory:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
