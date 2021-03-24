# ansible

> Gestionnaire de groupes d'ordinateurs à distance depuis SSH.
> Utiliser le fichier `/etc/ansible/hosts` pour ajouter de nouveaux groupes/hôtes.
> Plus d'information: <https://www.ansible.com/>.

- Lister les hôtes appartenant à un groupe :

`ansible {{group}} --list-hosts`

- Ping d'un groupe d'hôtes en invoquant le module "ping" :

`ansible {{group}} -m ping`

- Afficher des informations sur un groupe d'hôtes en invoquant le module "setup" :

`ansible {{group}} -m setup`

- Exécuter une commande sur un groupe d'hôtes en invoquant le module "command" avec des paramètres :

`ansible {{group}} -m command -a '{{my_command}}'`

- Exécuter une commande avec des droits administreur :

`ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'`

- Exécuter une commande en utilisant un fichier d'inventaire personnalisé :

`ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'`
