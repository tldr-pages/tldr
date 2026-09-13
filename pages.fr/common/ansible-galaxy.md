# ansible-galaxy

> Crée et gère les rôles Ansible.
> Plus d'informations : <https://docs.ansible.com/projects/ansible/latest/cli/ansible-galaxy.html>.

- Liste les rôles ou les collections installés :

`ansible-galaxy {{rôle|collection}} list`

- Recherche un rôle avec différents niveaux de verbosité (`-v` doit être spécifié à la fin) :

`ansible-galaxy role search {{mot_clé}} -v{{vvvvv}}`

- Installe ou enlève un/des rôle(s) :

`ansible-galaxy {{install|remove}} {{nom_du_rôle1 nom_du_rôle2 ...}}`

- Crée un nouveau rôle :

`ansible-galaxy init {{nom_du_rôle}}`

- Récupère les informations sur un rôle :

`ansible-galaxy role info {{nom_du_rôle}}`

- Installe ou enlève une/des collection(s) :

- ansible-galaxy collection {{install|remove}} {{nom_de_collection1 nom_de_collection2 ...}}

- Affiche l'aide sur les rôles ou les collections :

`ansible-galaxy {{rôle|collection}} {{[-h|--help]}}`
