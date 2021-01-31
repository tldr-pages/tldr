# git config

> Gérer les options de configuration personnalisées pour les référentiels Git.
> Ces configurations peuvent étre locales (pour le réferentiel courrant) ou globales (pour l utilisateur).
> Plus d'informations : <https://git-scm.com/docs/git-config>.

- Liste les entrés de configurations locales (stockés dans `.git/config` du repertoire courrant) :

`git config --list --local`

- Liste les entrés de conffigurations globales (stoqués dans `~/.gitconfig`) :

`git config --list --global`

- Liste toutes les entrés de conffiguration, globales et locales :

`git config --list`

- Recupére la valeure d'une entrée de configurations :

`git config alias.unstage`

- Attribue la valeur d'une entree de configuration :

`git config --global alias.unstage "reset HEAD --"`

- Restore la valeur d'une entree de configuration globale a sa valeur par défaut :

`git config --global --unset alias.unstage`

- Édite le fichier de configuration du référentiel courrant dans l'éditeur par défaut :

`git config --edit`

- Édite le fichier de configuration globale dans l'éditeur par défaut :

`git config --global --edit`
