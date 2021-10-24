# chown

> Modifie l'utilisateur et le groupe propriétaire des fichiers et dossiers.
> Plus d'informations : <https://www.gnu.org/software/coreutils/chown>.

- Modifie le propriétaire d'un fichier/dossier :

`chown {{utilisateur}} {{chemin/vers/fichier_ou_dossier}}`

- Modifie l'utilisateur et le groupe propriétaire d'un fichier/dossier :

`chown {{utilisateur}}:{{groupe}} {{chemin/vers/fichier_ou_dossier}}`

- Modifie récursivement le propriétaire d'un dossier et de son contenu :

`chown -R {{utilisateur}} {{chemin/vers/dossier}}`

- Modifie le propriétaire d'un lien symbolique :

`chown -h {{utilisateur}} {{chemin/vers/lien_symbolique}}`

- Modifie le propriétaire d'un fichier / dossier pour correspondre à un fichier de référence :

`chown --reference={{chemin/vers/fichier_de_référence}} {{chemin/vers/fichier_ou_dossier}}`
