# history expansion

> Réutiliser et développer l'historique des commandes shell dans `sh`, `bash`, `zsh`, `rbash` et `ksh`.
> Plus d'informations : <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Exécute de nouveau la commande précédente en tant que root (`!!` est remplacé par la commande précédente) :

`sudo !!`

- Exécute une commande avec le dernier argument de la commande précédente :

`{{commande}} !$`

- Exécute une commande avec le premier argument de la commande précédente :

`{{command}} !^`

- Exécute la `n`-ème commande de l'historique, en partant de la plus ancienne :

`!{{n}}`

- Exécute la `n`-ème commande de l'historique, en partant de la plus récente :

`!-{{n}}`

- Exécute la commande contenant `string` la plus récente :

`!?{{string}}?`

- Exécute la commande précédente, en remplaçant `string1` par `string2` :

`^{{string1}}^{{string2}}^`

- Effectue une expansion de l'historique, mais affiche la commande qui aurait du être exécutée au lieu de l'exécuter  :

`{{!-n}}:p`
