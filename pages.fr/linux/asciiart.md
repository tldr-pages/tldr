# asciiart

> Convertit des images en ASCII.
> Plus d'informations : <https://github.com/nodanaonlyzuul/asciiart>.

- Lit une image depuis un fichier et l'affiche en ASCII :

`asciiart {{chemin/vers/image.jpg}}`

- Lit une image depuis une URL et l'affiche en ASCII :

`asciiart {{www.example.com/image.jpg}}`

- Choisit la largeur de sortie (valeur par défaut : 100) :

`asciiart --width {{50}} {{chemin/vers/image.jpg}}`

- Colorise la sortie ASCII :

`asciiart --color {{chemin/vers/image.jpg}}`

- Choisit le format de sortie (format par défaut : textuel) :

`asciiart --format {{text|html}} {{chemin/vers/image.jpg}}`

- Inverse la table de caractères :

`asciiart --invert-chars {{chemin/vers/image.jpg}}`
