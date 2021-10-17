# tldr

> Afficher des pages d'aide simples pour des outils en ligne de commande, du projet tldr-pages.
> Plus d'informations : <https://tldr.sh>.

- Montrer la page tldr d'une commande (indication: c'est comme ça que vous êtes arrivé ici!) :

`tldr {{commande}}`

- Montrer la page tldr de `cd` en modifiant la plateforme par défaut :

`tldr -p {{android|linux|osx|sunos|windows}} {{cd}}`

- Montrer la page tldr d'une sous-commande :

`tldr {{git-checkout}}`

- Mettre à jour les pages locales (si le client a un cache):

`tldr -u`
