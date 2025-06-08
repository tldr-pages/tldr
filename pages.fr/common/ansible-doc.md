# ansible-doc

> Affiche les informations des modules installés dans les librairies Ansible.
> Affiche une liste concise des plugins et leurs description courte.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Liste les plugins action (modules) disponibles :

`ansible-doc {{[-l|--list]}}`

- Liste les plugins disponible d'un certain type :

`ansible-doc {{[-t|--type]}} {{type_de_plugin}} {{[-l|--list]}}`

- Affiche les informations sur un plugin action (module) spécifique :

`ansible-doc {{nom_du_plugin}}`

- Affiche les informations sur un plugin avec un certain type :

`ansible-doc {{[-t|--type]}} {{type_de_plugin}} {{nom_du_plugin}}`

- Affiche le raccourci playbook d'un plugin action (module) :

`ansible-doc {{[-s|--snippet]}} {{nom_du_plugin}}`

- Affiche les informations sur un plugin action (module) en JSON :

`ansible-doc {{[-j|--json]}} {{nom_du_plugin}}`
