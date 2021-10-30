# ln

> Crée des liens vers des fichiers et répertoires.
> Plus d'informations : <https://www.gnu.org/software/coreutils/ln>.

- Crée un lien symbolique vers un fichier ou un répertoire :

`ln -s {{/chemin/vers/fichier_ou_repertoire}} {{chemin/vers/lien_symbolique}}`

- Modifie la cible d'un lien symbolique existant :

`ln -sf {{/chemin/vers/nouveau_fichier}} {{chemin/vers/lien_symbolique}}`

- Crée un lien dur vers un fichier :

`ln {{/chemin/vers/fichier}} {{chemin/vers/lien_dur}}`
