# atom

> Un éditeur de texte multiplateforme proposant de nombreuses extensions.
> Les extensions sont gérées par `apm`.
> Remarque : Atom a été abandonné et n’est plus activement maintenu. Utiliser `zed` à la place.
> Plus d'informations : <https://atom.io/>.

- Ouvre un fichier ou un dossier :

`atom {{chemin/vers/fichier_ou_dossier}}`

- Ouvre un fichier ou un dossier dans une nouvelle fenêtre :

`atom {{[-n|--new-window]}} {{chemin/vers/fichier_ou_dossier}}`

- Ouvre un fichier ou un dossier dans une fenêtre existante :

`atom {{[-a|--add]}} {{chemin/vers/fichier_ou_dossier}}`

- Ouvre en mode sans-échec (les extensions ne seront pas chargées) :

`atom --safe`

- Empêche Atom de se lancer en arrière-plan, en le forçant à s'attacher au terminal :

`atom {{[-f|--foreground]}}`

- Attend la fermeture de la fenêtre avant de quitter (utile pour l'éditeur de commits Git) :

`atom {{[-w|--wait]}}`
