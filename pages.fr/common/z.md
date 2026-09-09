# z

> Recherche les répertoires les plus utilisés et permet une navigation rapide à l'aide de chaînes de caractères ou de `regex`.
> Plus d'informations : <https://github.com/rupa/z>.

- Navigue vers un répertoire qui contient `string` dans son nom :

`z string`

- Navigue vers un répertoire qui contient `string1` puis `string2` :

`z string1 string2`

- Navigue vers le répertoire le mieux classé parmi ceux qui contiennent `string` dans leurs noms :

`z -r string`

- Navigue vers le répertoire accédé le plus récemment parmi ceux qui contiennent `string` dans leurs noms :

`z -t string`

- Liste l'ensemble des dossiers dans la base de données `z` qui contiennent `string` dans leurs noms :

`z -l string`

- Supprime le dossier actuel de la base de données de `z` :

`z -x`

- Restreint les correspondances aux sous-répertoires du répertoire actuel :

`z -c {{string}}`
