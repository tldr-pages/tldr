# babel

> Un transpilateur qui convertit du code JavaScript avec la syntaxe ES6/ES7 en syntaxe ES5.
> Plus d'informations : <https://babeljs.io/>.

- Transpile une fichier spécifié et affiche le résultat dans la sortie standard :

`babel {{chemin/vers/fichier}}`

- Transpile un fichier spécifié et enregistre le résultat dans un autre fichier :

`babel {{chemin/vers/fichier/d_entrée}} --out-file {{chemin/vers/fichier/de/sortie}}`

- Transpile un fichier d'entrée à chaque fois qu'il est modifié :

`babel {{chemin/vers/fichier/d_entrée}} --watch`

- Transpile tout un dossier et ses fichiers :

`babel {{chemin/vers/dossier}}`

- Ignore des fichiers (séparés par une virgule) dans un dossier :

`babel {{chemin/vers/dossier}} --ignore {{fichiers_ignorés}}`

- Transpile et minifie la sortie :

`babel {{chemin/vers/fichier/d_entrée}} --minified`

- Sélectionne un lot de pré-configuration pour le formatage de sortie :

`babel {{chemin/vers/fichier/d_entrée}} --presets {{pré-configurations}}`

- Affiche toutes les options disponibles :

`babel --help`
