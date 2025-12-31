# ls

> Liste le contenu d'un répertoire.
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Liste les fichiers, un par ligne :

`ls -1`

- Liste tous les fichiers, ainsi que les fichiers cachés :

`ls {{[-a|--all]}}`

- Liste tous les fichiers, avec les noms de répertoires suivis d'un `/` :

`ls {{[-F|--classify]}}`

- Liste tous les fichiers avec un format détaillé (permissions, propriétaire, taille et date de modification) :

`ls {{[-la|--all -l]}}`

- Liste les fichiers avec un format détaillé en utilisant des préfixes d'unités (KiB, MiB, GiB) :

`ls {{[-lh|-l --human-readable]}}`

- Liste les fichiers avec un format détaillé en triant par taille décroissante :

`ls {{-lSR|-lS --recursive}}`

- Liste avec un format détaillé tous les fichiers en triant par date de modification (les plus anciennes en premier) :

`ls {{[-ltr|-lt --reverse]}}`

- Liste uniquement les répertoires :

`ls {{[-d|--directory]}} */`
