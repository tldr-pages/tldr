# ansible-playbook

> Esegui task definiti nel playbook su macchine remote via SSH.
> Maggiori informazioni: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-playbook.html>.

- Esegui task nel playbook:

`ansible-playbook {{playbook}}`

- Esegui task nel playbook con inventory host personalizzato:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{file_inventory}}`

- Esegui task nel playbook con variabili extra definite da linea di comando:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{variabile1}}={{valore1}} {{variabile2}}={{valore2}}"`

- Esegui task nel playbook con variabili extra definite in un file JSON:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{variabili.json}}"`

- Esegui task nel playbook per i tag specificati:

`ansible-playbook {{playbook}} {{[-t|--tags]}} {{tag1,tag2}}`

- Esegui task nel playbook partendo da un task specifico:

`ansible-playbook {{playbook}} --start-at {{nome_task}}`

- Esegui task nel playbook senza apportare modifiche (dry-run):

`ansible-playbook {{playbook}} {{[-C|--check]}} {{[-D|--diff]}}`
