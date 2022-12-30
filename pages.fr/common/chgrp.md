# chgrp

> Change la propriété de groupe des fichiers et des répertoires.
> Plus d'informations : <https://www.gnu.org/software/coreutils/chgrp>.

- Change le groupe propriétaire d'un fichier/répertoire :

`chgrp {{groupe}} {{chemin/vers/fichier_ou_répertoire}}`

- Change récursivement le groupe propriétaire d'un répertoire et de son contenu :

`chgrp -R {{groupe}} {{chemin/vers/répertoire}}`

- Change le groupe propriétaire d'un lien symbolique :

`chgrp -h {{groupe}} {{chemin/vers/lien_symbolique}}`

- Modifie le groupe propriétaire d'un fichier/répertoire pour qu'il corresponde à un fichier de référence :

`chgrp --reference={{chemin/vers/fichier_référence}} {{chemin/vers/fichier_ou_répertoire}}`
