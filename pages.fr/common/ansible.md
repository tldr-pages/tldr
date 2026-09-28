# ansible

> Gestionnaire de groupes d'ordinateurs à distance depuis SSH. (Utiliser le fichier `/etc/ansible/hosts` pour ajouter de nouveaux groupes/hôtes).
> Certaines commandes comme `ansible galaxy` ont leur propre documentation.
> Plus d'informations : <https://docs.ansible.com/projects/ansible/latest/cli/ansible.html>.

- Liste les hôtes appartenant à un groupe :

`ansible {{groupe}} --list-hosts`

- Ping d'un groupe d'hôtes en invoquant le [m]odule "ping" :

`ansible {{groupe}} {{[-m|--module-name]}} ping`

- Affiche des informations sur un groupe d'hôtes en invoquant le [m]odule "setup" :

`ansible {{groupe}} {{[-m|--module-name]}} setup`

- Exécute une commande sur un groupe d'hôtes en invoquant le [m]odule "command" avec en paramètre (a) cette commande :

`ansible {{groupe}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{ma_commande}}'`

- Exécute une commande avec des droits administrateur :

`ansible {{groupe}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{ma_commande}}'`

- Exécute une commande en utilisant un fichier d'inventaire personnalisé :

`ansible {{groupe}} {{[-i|--inventory]}} {{fichier_d'inventaire}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{ma_commande}}'`

- Liste les groupes d'un inventaire :

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
