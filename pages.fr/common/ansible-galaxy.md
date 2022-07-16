# ansible-galaxy

> Crée et gère les rôles Ansible.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Installe un rôle :

`ansible-galaxy install {{nom_d_utilisateur}}.{{nom_du_rôle}}`

- Enlève un rôle :

`ansible-galaxy remove {{nom_d_utilisateur}}.{{nom_du_rôle}}`

- Liste les rôles installés :

`ansible-galaxy list`

- Recherche pour un role donné :

`ansible-galaxy search {{nom_du_rôle}}`

- Crée un nouveau rôle :

`ansible-galaxy init {{nom_du_rôle}}`

- Récupère les informations sur le rôle d'un utilisateur :

`ansible-galaxy role info {{nom_d_utilisateur}}.{{nom_du_rôle}}`

- Récupère les informations d'une collection :

`ansible-galaxy collection info {{nom_d_utilisateur}}.{{nom_de_la_collection}}`
