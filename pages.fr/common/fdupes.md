# fdupes

> Trouve les fichiers dupliqués dans les répertoires donnés.
> Plus d'informations : <https://github.com/adrianlopezroche/fdupes#introduction>.

- Cherche dans un répertoire :

`fdupes {{chemin/vers/répertoire}}`

- Cherche dans plusieurs répertoires :

`fdupes {{répertoire1}} {{répertoire2}}`

- Cherche dans un répertoire récursivement :

`fdupes -r {{répertoire}}`

- Cherche dans plusieurs répertoires dont un récursivement :

`fdupes {{répertoire2}} -R {{répertoire2}}`

- Cherche récursivement les dupliqués et demande les fichiers à conserver, supprimant les autres :

`fdupes -rd {{répertoire}}`

- Cherche récursivement et supprime les dupliqués automatiquement :

`fdupes -rdN {{répertoire}}`
