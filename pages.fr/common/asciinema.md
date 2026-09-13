# asciinema

> Enregistre et rejoue les sessions de terminal, et également partageable sur asciinema.org.
> Voir aussi : `terminalizer`, `agg`.
> Plus d'informations : <https://docs.asciinema.org/manual/cli/>.

- Associe l’installation locale de `asciinema` avec un compte asciinema.org :

`asciinema {{[a|auth]}}`

- Crée un nouvel enregistrement et l'enregistre dans un fichier local (finir avec `Ctrl d` ou taper `exit`):

`asciinema {{[r|record]}} {{chemin/vers/enregistrement.cast}}`

- Rejoue un enregistrement depuis un fichier local :

`asciinema {{[p|play]}} {{chemin/vers/enregistrement.cast}}`

- Rejoue un enregistrement depuis <https://asciinema.org> :

`asciinema {{[p|play]}} https://asciinema.org/a/{{id_d_enregistrement}}`

- Crée un nouvel enregistrement, en limitant le temps d’inactivité au maximum à 2.5 secondes :

`asciinema {{[r|record]}} {{[-i|--idle-time-limit]}} 2.5`

- Affiche la sortie complète d'un enregistrement local :

`asciinema {{[ca|cat]}} {{chemin/vers/enregistrement.cast}}`

- Envoie un enregistrement local vers asciinema.org :

`asciinema {{[u|upload]}} {{chemin/vers/enregistrement.cast}}`

- Diffuse le terminal actuel sur une page web locale :

`asciinema {{[st|stream]}} --local`