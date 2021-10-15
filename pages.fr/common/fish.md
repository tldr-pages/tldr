# fish

> Friendly Interactive SHell, un interpréteur de ligne de commande, conçu pour être facile à utiliser.
> Plus d'informations : <https://fishshell.com>.

- Démarrer une session shell interactive :

`fish`

- Exécuter une commande, puis terminer la session :

`fish -c "{{commande}}"`

- Exécuter un script :

`fish {{chemin/vers/le/script.fish}}`

- Vérifier les erreurs de syntaxe dans un script :

`fish --no-execute {{chemin/vers/le/script.fish}}`

- Démarrer une session shell interactive en mode privé, dans laquelle le shell n'a pas accès à l'historique et n'y écrit rien :

`fish --private`

- Afficher les informations de version :

`fish --version`

- Ajouter et exporter une variable d'environnement, qui persiste entre les redémarrages du shell (exécuter depuis le shell uniquement) :

`set -Ux {{nom_de_la_variable}} {{valeur_de_la_variable}}`
