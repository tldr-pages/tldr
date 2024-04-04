# ansible-inventory

> Display or dump an Ansible inventory.
> Voir aussi : `ansible`.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Affiche l'inventaire par défaut :

`ansible-inventory --list`

- Affiche un inventaire spécifique :

`ansible-inventory --list --inventory {{chemin/vers/fichier_ou_script_ou_dossier}}`

- Affiche l'inventaire par défaut en YAML :

`ansible-inventory --list --yaml`

- Sauvegarde l'inventaire par défaut dans un fichier :

`ansible-inventory --list --output {{chemin/vers/fichier}}`
