# ansible-pull

> Scarica playbook Ansible da un repository VCS ed eseguili per l'host locale.
> Maggiori informazioni: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-pull.html>.

- Scarica un playbook da VCS ed esegui il playbook `local.yml` predefinito:

`ansible-pull {{[-U|--url]}} {{url_repository}}`

- Scarica un playbook da VCS ed esegui un playbook specifico:

`ansible-pull {{[-U|--url]}} {{url_repository}} {{playbook}}`

- Scarica un playbook da VCS da un branch specifico ed esegui un playbook specifico:

`ansible-pull {{[-U|--url]}} {{url_repository}} {{[-C|--checkout]}} {{branch}} {{playbook}}`

- Scarica un playbook da VCS, specifica file host ed esegui un playbook specifico:

`ansible-pull {{[-U|--url]}} {{url_repository}} {{[-i|--inventory-file]}} {{file_host}} {{playbook}}`
