# ruby

> Interpréteur du langage de programmation Ruby.
> Voir aussi : `gem`, `bundler`, `rake`, `irb`.
> Plus d'informations : <https://www.ruby-lang.org>.

- Exécute un script Ruby :

`ruby {{script.rb}}`

- Exécute une seule commande Ruby dans la ligne de commande :

`ruby -e {{commande}}`

- Vérifie les erreurs de syntaxe d'un script Ruby donné :

`ruby -c {{script.rb}}`

- Démarre le serveur HTTP intégré sur le port 8080 dans le répertoire actuel :

`ruby -run -e httpd`

- Exécute localement un binaire Ruby sans installer la bibliothèque requise dont il dépend :

`ruby -I {{chemin/vers/dossier_bibliothèque}} -r {{nom_chargement_bibliothèque}} {{chemin/vers/dossier_bin/nom_bin}}`

- Affiche la version de Ruby utilisée :

`ruby -v`
