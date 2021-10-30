# ansible

> Gestionnaire de groupes d'ordinateurs à distance depuis SSH. (Utiliser le fichier `/etc/ansible/hosts` pour ajouter de nouveaux groupes/hôtes).
> Certaines commandes comme `ansible galaxy` ont leur propre documentation.
> Plus d'informations : <https://www.ansible.com/>.

- Lister les hôtes appartenant à un groupe :

`ansible {{groupe}} --list-hosts`

- Ping d'un groupe d'hôtes en invoquant le [m]odule "ping" :

`ansible {{groupe}} -m ping`

- Afficher des informations sur un groupe d'hôtes en invoquant le [m]odule "setup" :

`ansible {{groupe}} -m setup`

- Exécuter une commande sur un groupe d'hôtes en invoquant le [m]odule "command" avec en paramètre (a) cette commande :

`ansible {{groupe}} -m command -a '{{ma_commande}}'`

- Exécuter une commande avec des droits administrateur :

`ansible {{groupe}} --become --ask-become-pass -m command -a '{{ma_commande}}'`

- Exécuter une commande en utilisant un fichier d'inventaire personnalisé :

`ansible {{groupe}} -i {{fichier_d'inventaire}} -m command -a '{{ma_commande}}'`

- Lister les groupes d'un inventaire :

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
