# chmod

> Modifie les droits d'accès d'un fichier ou d'un répertoire.
> Plus d'informations : <https://www.gnu.org/software/coreutils/chmod>.

- Donne les droits d'e[x]écution à l'[u]tilisateur auquel le fichier appartient :

`chmod u+x {{fichier}}`

- Donne à l'utilisateur les droits de lecture (r) et d'écriture (w) sur un fichier/répertoire :

`chmod u+rw {{fichier_ou_repertoire}}`

- Enlève les droits d'exécution pour le [g]roupe :

`chmod g-x {{fichier}}`

- Donne à tous (a) les utilisateurs les droits de lecture et d'exécution :

`chmod a+rx {{fichier}}`

- Donne aux autres utilisateurs (qui sont dans un autre groupe) les mêmes droits que ceux du groupe propriétaire :

`chmod o=g {{fichier}}`

- Retire tous les droits aux autres (o) utilisateurs :

`chmod o= {{fichier}}`

- Modifie les permissions récursivement en donnant aux membres du groupe et aux autres utilisateurs le droit d'écriture :

`chmod -R g+w,o+w {{repertoire}}`
