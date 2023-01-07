# chmod

> Modifie les droits d'accès d'un fichier ou d'un répertoire.
> Plus d'informations : <https://www.gnu.org/software/coreutils/chmod>.

- Donne les droits d'e[x]écution à l'[u]tilisateur auquel le fichier appartient :

`chmod u+x {{chemin/vers/fichier}}`

- Donne à l'[u]tilisateur les droits de lecture [r] et d'écriture [w] sur un fichier/répertoire :

`chmod u+rw {{chemin/vers/fichier_ou_répertoire}}`

- Enlève les droits d'e[x]écution pour le [g]roupe :

`chmod g-x {{chemin/vers/fichier}}`

- Donne à tous [a] les utilisateurs les droits de lecture [r] et d'e[x]écution :

`chmod a+rx {{chemin/vers/fichier}}`

- Donne aux autres [o] utilisateurs (qui sont dans un autre groupe) les mêmes droits que ceux du [g]roupe propriétaire :

`chmod o=g {{chemin/vers/fichier}}`

- Retire tous les droits aux autres [o] utilisateurs :

`chmod o= {{chemin/vers/fichier}}`

- Modifie les permissions récursivement en donnant aux membres du [g]roupe et aux autres [o] utilisateurs le droit d'écriture [w] :

`chmod -R g+w,o+w {{chemin/vers/répertoire}}`

- Donne récursivement à tous [a] les utilisateurs les droits de lecture [r] de fichiers et d'e[X]écution de sous-répertoires à l'intérieur d'un répertoire :

`chmod -R a+rX {{chemin/vers/répertoire}}`
