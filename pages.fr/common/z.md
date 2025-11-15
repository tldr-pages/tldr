# z

> Recherche les répertoires les plus utilisés et permet une navigation rapide à l'aide de chaînes de caractères ou d'expressions régulières.
> Plus d'informations : <https://github.com/rupa/z>.

- Aller dans un répertoire qui contient "foo" dans son nom :

`z {{foo}}`

- Aller dans un répertoire qui contient "foo" et "bar' dans son nom :

`z {{foo}} {{bar}}`

- Aller dans le répertoire le mieux classé parmi ceux qui contiennent "foo" dans leurs noms :

`z -r {{foo}}`

- Aller dans le répertoire accédé le plus récemment parmi ceux qui contiennent "foo" dans leurs noms :

`z -t {{foo}}`

- Lis l'ensemble des répertoires dans la base de données `z` qui contiennent "foo" dans leurs noms :

`z -l {{foo}}`

- Supprime le répertoire courant de la base de données de `z` :

`z -x .`
