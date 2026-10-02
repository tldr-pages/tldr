# agg

> Crée un GIF à partir d'un enregistrement de session de terminal `asciinema`.
> Plus d'informations : <https://docs.asciinema.org/manual/agg/usage/>.

- Crée un GIF :

`agg {{chemin/vers/demo.cast}} {{chemin/vers/demo.gif}}`

- Crée un GIF de 80 colonnes de largeur et de 25 lignes de hauteur :

`agg --cols 80 --rows 25 {{chemin/vers/demo.cast}} {{chemin/vers/demo.gif}}`

- Crée un GIF avec une taille de police de 24 pixels :

`agg --font-size 24 {{chemin/vers/demo.cast}} {{chemin/vers/demo.gif}}`

- Affiche l'aide :

`agg {{[-h|--help]}}`
