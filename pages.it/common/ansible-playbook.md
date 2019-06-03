# ansible-playbook

> Esegui task definiti nel playbook di un computer remoto via SSH.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Esegui tasks nel playbook:

`ansible-playbook {{playbook}}`

- Esegui task nel playbook con un inventory personalizzato:

`ansible-playbook {{playbook}} -i {{inventory}}`

- Esegui task nel playvook con variabili aggiuntive definite da linea di comando:

`ansible-playbook {{playbook}} -e "{{variabile1}}={{valore1}} {{variabile2}}={{valore2}} ..."`

- Esegui task nel playbook con variabili aggiuntive definite in un file JSON:

`ansible-playbook {{playbook}} -e "@{{variabili.json}}"`
