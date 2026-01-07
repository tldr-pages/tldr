# asciiart

> Convertit des images en ASCII.
> Plus d'informations : <https://github.com/nodanaonlyzuul/asciiart#in-the-command-line>.

- Lit une image depuis un fichier et l'affiche en ASCII :

`asciiart {{chemin/vers/image.jpg}}`

- Lit une image depuis une URL et l'affiche en ASCII :

`asciiart {{www.example.com/image.jpg}}`

- Choisit la largeur de sortie (valeur par défaut : 100) :

`asciiart {{[-w|--width]}} {{50}} {{chemin/vers/image.jpg}}`

- Colorise la sortie ASCII :

`asciiart {{[-c|--color]}} {{chemin/vers/image.jpg}}`

- Choisit le format de sortie (format par défaut : textuel) :

`asciiart {{[-f|--format]}} {{text|html}} {{chemin/vers/image.jpg}}`

- Inverse la table de caractères :

`asciiart {{[-i|--invert-chars]}} {{chemin/vers/image.jpg}}`
