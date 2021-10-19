# fish

> Friendly Interactive SHell, un interpréteur de ligne de commande, conçu pour être facile à utiliser.
> Plus d'informations : <https://fishshell.com>.

- Démarre une session shell interactive :

`fish`

- Exécute une commande, puis termine la session :

`fish -c "{{commande}}"`

- Exécute un script :

`fish {{chemin/vers/le/script.fish}}`

- Vérifie les erreurs de syntaxe dans un script :

`fish --no-execute {{chemin/vers/le/script.fish}}`

- Démarre une session shell interactive en mode privé, dans laquelle le shell n'a pas accès à l'historique et n'y écrit rien :

`fish --private`

- Affiche les informations de version :

`fish --version`

- Ajoute et exporte une variable d'environnement, qui persiste entre les redémarrages du shell (à exécuter depuis le shell uniquement) :

`set -Ux {{nom_de_la_variable}} {{valeur_de_la_variable}}`
