# ansible-pull

> Récupère les playbook ansible depuis un dépôt VCS et exécute les en local.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Récupère le playbook depuis un VCS et exécute le fichier par défaut local.yaml du playbook :

`ansible-pull -U {{url_du_dépôt}}`

- Récupère le playbook depuis un VCS et exécute un playbook spécifique :

`ansible-pull -U {{url_du_dépôt}} {{playbook}}`

- Récupère un playbook depuis un VCS sur une branche spécifique et exécute ce dernier :

`ansible-pull -U {{url_du_dépôt}} -C {{branche}} {{playbook}}`

- Récupère un playbook depuis un VCS, spécifie les fichiers hôtes et exécute un playbook spécifique :

`ansible-pull -U {{url_du_dépôt}} -i {{fichier_hôtes}} {{playbook}}`
