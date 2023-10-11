# ark

> Outil d'archive de KDE.
> Plus d'informations : <https://docs.kde.org/stable5/en/ark/ark/>.

- Extrait une archive dans le répertoire courant :

`ark --batch {{chemin/vers/archive}}`

- Change le répertoire d'extraction :

`ark --batch --destination {{chemin/vers/dossier}} {{chemin/vers/archive}}`

- Crée une archive si elle n'existe pas et y ajouter des fichiers :

`ark --add-to {{chemin/vers/archive}} {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`
