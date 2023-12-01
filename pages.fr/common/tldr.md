# tldr

> Affiche des pages d'aide simples pour les outils en ligne de commande, depuis le projet `tldr-pages`.
> Plus d'informations : <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Affiche la page tldr d'une commande (indice : c'est comme ça que vous êtes arrivé ici !) :

`tldr {{commande}}`

- Affiche la page tldr de `cd`, en forçant la plateforme par défaut :

`tldr -p {{android|linux|osx|sunos|windows}} {{cd}}`

- Affiche la page tldr d'une sous-commande :

`tldr {{git-checkout}}`

- Met à jour les pages enregistrées localement (si le client supporte la mise en cache) :

`tldr -u`
