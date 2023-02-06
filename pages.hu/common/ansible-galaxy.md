# ansible-galaxy

> Ansible-szerepek létrehozása és kezelése. További információ: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Telepítsen egy szerepet:

`ansible-galaxy install {{username}}.{{role_name}}`

- Szerepkör eltávolítása:

`ansible-galaxy remove {{username}}.{{role_name}}`

- Telepített szerepek listázása:

`ansible-galaxy list`

- Egy adott szerepkör keresése:

`ansible-galaxy search {{role_name}}`

- Új szerepkör létrehozása:

`ansible-galaxy init {{role_name}}`

- Információk lekérdezése egy felhasználói szerepkörről:

`ansible-galaxy role info {{username}}.{{role_name}}`

- Információk lekérdezése egy gyűjteményről:

`ansible-galaxy collection info {{username}}.{{collection_name}}`
