# chmod

> Modifie les droits d'accès d'un fichier ou d'un répertoire.

- Donne les droits d'e[x]écution à l'[u]tilisateur auquel le fichier appartient:

`chmod u+x {{fichier}}`

- Donne à l'utilisateur les droits de lecture (r) et d'écriture (w) sur un fichier/répertoire:

`chmod u+rw {{fichier_ou_repertoire}}`

- Enlève les droits d'exécution pour le [g]roupe:

`chmod g-x {{fichier}}`

- Donne à tous (a) les utilisateurs les droits de lecture et d'exécution:

`chmod a+rx {{fichier}}`

- Donne aux autres utilisateurs (qui ne sont pas dans le même que le propriétaire du fichier) les même droits que ceux du groupe:

`chmod o=g {{fichier}}`

- Modifie les permissions recursivement en donnant aux membres du groupe et aux autres utilisateurs le droit d'écriture:

`chmod -R g+w,o+w {{directory}}`
