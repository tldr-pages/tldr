# atuin

> Enregistre votre historique shell dans une base de donnée.
> Peut également synchroniser votre historique chiffré entre plusieurs machines.
> Plus d'informations : <https://atuin.sh/docs/commands>.

- Installe atuin dans votre shell :

`eval "$(atuin init {{bash|zsh|fish}})"`

- Importe l'historique du shell par défaut :

`atuin import auto`

- Recherche dans l'historique shell une commande spécifique :

`atuin search {{commande}}`

- Inscrire un compte sur le serveur de synchronisation par défaut :

`atuin register -u {{nom_d_utilisateur}} -e {{email}} -p {{mot_de_passe}}`

- Connexion au serveur de synchronisation par défaut :

`atuin login -u {{nom_d_utilisateur}} -p {{mot_de_passe}}`

- Synchronise l'historique avec le serveur :

`atuin sync`
