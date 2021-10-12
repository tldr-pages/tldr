# ssh-add

> Gère les clés SSH enregistrées dans l'agent SSH `ssh-agent`.
> S'assurer que `ssh-agent` est en fonctionnement pour enregistrer des clés.
> Plus d'informations : <https://man.openbsd.org/ssh-add>.

- Ajouter les clés présentes dans `~/.ssh` (clés par défaut) à l'agent SSH :

`ssh-add`

- Ajouter une clé spécifique à l'agent SSH :

`ssh-add {{chemin/vers/clé_privée}}`

- Lister les empreintes des clés actuellement enregistrées :

`ssh-add -l`

- Supprimer une clé de l'agent SSH :

`ssh-add -d {{chemin/vers/clé_privée}}`

- Supprimer toutes les clés enregistrées de l'agent SSH :

`ssh-add -D`

- Ajouter une clé spécifique à l'agent SSH et au trousseau de clés :

`ssh-add -K {{chemin/vers/clé_privée}}`
