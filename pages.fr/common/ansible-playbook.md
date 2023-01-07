# ansible-playbook

> Exécute les tâches définies dans le playbook sur les machines distantes via SSH.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Exécute les tâches d'un playbook :

`ansible-playbook {{playbook}}`

- Exécute les tâches d'un playbook avec fichier d'inventaire spécifié :

`ansible-playbook {{playbook}} -i {{fichier_d_inventaire}}`

- Exécute les tâches d'un playbook avec des variables supplémentaires définies via la ligne de commande :

`ansible-playbook {{playbook}} -e "{{variable1}}={{valeur1}} {{variable2}}={{valeur2}}"`

- Exécute les tâches d'un playbook avec des variables supplémentaires définies dans un fichier JSON :

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`

- Exécute les tâches d'un playbook pour certain tags :

`ansible-playbook {{playbook}} --tags {{tag1,tag2}}`

- Exécute les tâches d'un playbook en démarrant depuis une certaine tache :

`ansible-playbook {{playbook}} --start-at {{nom_de_la_tache}}`
