# apt-get

> Utilitaire de gestion des paquets Debian et Ubuntu.
> Recherche des paquets en utilisant `apt-cache`.
> Plus d'informations : <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Mise à jour de la liste des paquets et des versions disponibles (il est recommandé de l'exécuter avant les autres commandes `apt-get`) :

`apt-get update`

- Installation d'un paquet, ou mise à jour avec la dernière version disponible :

`apt-get install {{package}}`

- Suppression d'un paquet :

`apt-get remove {{package}}`

- Suppression d'un paquet et de ses fichiers de configuration :

`apt-get purge {{package}}`

- Mise à jour de tous les paquets installés vers les dernières versions disponibles :

`apt-get upgrade`

- Nettoyage du dépôt local - supprime les fichiers de paquets (`.deb`) des téléchargements interrompus qui ne peuvent plus être téléchargés :

`apt-get autoclean`

- Suppression de tous les paquets qui ne sont plus nécessaires :

`apt-get autoremove`

- Mise à jour des paquets installés (comme la commande `upgrade`), mais avec suppression des paquets obsolètes et installation des paquets supplémentaires pour répondre aux nouvelles dépendances :

`apt-get dist-upgrade`
