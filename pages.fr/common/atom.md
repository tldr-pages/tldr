# atom

> Un éditeur de texte multiplateforme proposant de nombreuses extensions.
> Les extensions sont gérées par `apm`.
> Plus d'informations : <https://atom.io/>.

- Ouvrir un fichier ou un dossier :

`atom {{chemin/vers/fichier_ou_dossier}}`

- Ouvrir un fichier ou un dossier dans une nouvelle fenêtre :

`atom -n {{chemin/vers/fichier_ou_dossier}}`

- Ouvrir un fichier ou un dossier dans une fenêtre existante :

`atom --add {{chemin/vers/fichier_ou_dossier}}`

- Ouvrir en mode sans-échec (les extensions ne seront pas chargées) :

`atom --safe`

- Empêcher Atom de se lancer en arrière-plan, en le forçant à s'attacher au terminal :

`atom --foreground`

- Attendre la fermeture de la fenêtre avant de quitter (utile pour l'éditeur de commits Git) :

`atom --wait`
