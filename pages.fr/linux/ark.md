# ark

> Outil d'archive de KDE.
> Plus d'informations : <https://docks.kde.org/stable5/en/ark/ark/>.

- Extrait une archive dans le répertoire courant :

`ark --batch {{archive}}`

- Change le répertoire d'extraction :

`ark --batch --destination {{chemin/vers/le/répertoire}} {{archive}}`

- Crée une archive si elle n'existe pas et y ajouter des fichiers :

`ark --add-to {{archive}} {{fichier1}} {{fichier2}} ...`
