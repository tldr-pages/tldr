# mktemp

> Crée un fichier ou un répertoire temporaire.
> Plus d'informations : <https://man.openbsd.org/mktemp.1>.

- Crée un fichier temporaire vide et affiche son chemin d'accès absolu :

`mktemp`

- Utilise un répertoire personnalisé si `$TMPDIR` n'est pas défini (la valeur par défaut dépend de la plateforme, mais est habituellement `/tmp`) :

`mktemp -p {{/chemin/vers/reptemp}}`

- Utilise un modèle de chemin personnalisé (les `X` sont remplacés par des caractères alphanumériques aléatoires) :

`mktemp {{/tmp/exemple.XXXXXXXX}}`

- Utilise un modèle de nom de fichier personnalisé :

`mktemp -t {{exemple.XXXXXXXX}}`

- Crée un répertoire temporaire vide et affiche son chemin d'accès absolu :

`mktemp -d`
