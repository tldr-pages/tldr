# zola

> Un générateur de site statique à partir d'un unique binaire sans dépendance.
> Plus d'informations : <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- Créer la structure du répertoire utilisé par Zola dans un répertoire donné :

`zola init {{mon_site}}`

- Construit la totalité du site dans le répertoire `public` (si le répertoire existe, il est supprimé) :

`zola build`

- Construit la totalité du site dans un répertoire différent :

`zola build --output-dir {{chemin/du/répertoire_de_sortie/}}`

- Construit et met à disposition le site à partir d'un serveur local (l'adresse par défaut est `127.0.0.1:1111`) :

`zola serve`

- Construit l'ensemble des pages comme la commande `build`, sans écrire le résultat sur le disque :

`zola check`
