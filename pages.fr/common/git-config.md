# git config

> Gérer les options de configuration personnalisées pour les référentiels Git.
> Ces configurations peuvent être locales (pour le référentiel courant) ou globales (pour l'utilisateur).
> Plus d'informations : <https://git-scm.com/docs/git-config>.

- Liste les entrées de configurations locales (stockées dans `.git/config` du répertoire courant) :

`git config --list --local`

- Liste les entrées de configuration globales (stockées dans `~/.gitconfig`) :

`git config --list --global`

- Récupère la valeur d'une entrée de configuration :

`git config alias.unstage`

- Attribue la valeur d'une entrée de configuration :

`git config --global alias.unstage "reset HEAD --"`

- Restaure la valeur d'une entrée de configuration globale à sa valeur par défaut :

`git config --global --unset alias.unstage`

- Édite le fichier de configuration du référentiel courant dans l'éditeur par défaut :

`git config --edit`

- Édite le fichier de configuration globale dans l'éditeur par défaut :

`git config --global --edit`
