# ansible

> Gestionnaire de groupes d'ordinateurs à distance depuis SSH. (Utiliser le fichier `/etc/ansible/hosts` pour ajouter de nouveaux groupes/hôtes).
> Certaines commandes comme `ansible galaxy` ont leur propre documentation.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Lister les hôtes appartenant à un groupe :

`ansible {{groupe}} --list-hosts`

- Ping d'un groupe d'hôtes en invoquant le [m]odule "ping" :

`ansible {{groupe}} {{[-m|--module-name]}} ping`

- Afficher des informations sur un groupe d'hôtes en invoquant le [m]odule "setup" :

`ansible {{groupe}} {{[-m|--module-name]}} setup`

- Exécuter une commande sur un groupe d'hôtes en invoquant le [m]odule "command" avec en paramètre (a) cette commande :

`ansible {{groupe}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{ma_commande}}'`

- Exécuter une commande avec des droits administrateur :

`ansible {{groupe}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{ma_commande}}'`

- Exécuter une commande en utilisant un fichier d'inventaire personnalisé :

`ansible {{groupe}} {{[-i|--inventory]}} {{fichier_d'inventaire}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{ma_commande}}'`

- Lister les groupes d'un inventaire :

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
