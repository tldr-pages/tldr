# tldr

> Affiche des pages d'aide simples pour les outils en ligne de commande, depuis le projet `tldr-pages`.
> Plus d'informations : <https://tldr.sh>.

- Afficher la page tldr d'une commande (indice : c'est comme ça que vous êtes arrivé ici !) :

`tldr {{commande}}`

- Afficher la page tldr de `cd`, en forçant la plateforme par défaut :

`tldr -p {{android|linux|osx|sunos|windows}} {{cd}}`

- Afficher la page tldr d'une sous-commande :

`tldr {{git-checkout}}`

- Mettre à jour les pages enregistrées localement (si le client supporte la mise en cache) :

`tldr -u`
