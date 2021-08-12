# ansible-galaxy

> Creați și gestionați roluri Ansible.
> Mai multe informaţii: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>

- Instalați un rol:

`ansible-galaxy install {{username}}.{{role_name}}`

- Elimină un rol:

`ansible-galaxy remove {{username}}.{{role_name}}`

- Lista rolurilor instalate:

`ansible-galaxy list`

- Caută un rol dat:

`ansible-galaxy search {{role_name}}`

- Crearea unui nou rol:

`ansible-galaxy init {{role_name}}`

- Obțineți informații despre un rol de utilizator:

`ansible-galaxy role info {{username}}.{{role_name}}`

- Obțineți informații despre o colecție:

`ansible-galaxy collection info {{username}}.{{collection_name}}`
