# bundle

> Gestionnaire de dépendances pour le langage de programmation Ruby.
> Plus d'informations : <https://bundler.io/man/bundle.1.html>.

- Installe toutes les gems définies dans le `Gemfile` attendu dans le répertoire de travail :

`bundle install`

- Exécute une commande dans le contexte du bundle actuel :

`bundle exec {{commande}} {{arguments}}`

- Mets à jour toutes les gems selon les règles définies dans le `Gemfile` et régénére le fichier `Gemfile.lock` :

`bundle update`

- Mets à jour une ou plusieurs gem(s) spécifique(s) définie(s) dans le `Gemfile` :

`bundle update {{nom_de_la_gem}} {{nom_de_la_gem}}`

- Mets à jour une ou plusieurs gem(s) spécifique(s) définie(s) dans le `Gemfile` mais seulement vers la prochaine version de patch :

`bundle update --patch {{nom_de_la_gem}} {{nom_de_la_gem}}`

- Mets à jour toutes les gem(s) du groupe donné dans le `Gemfile` :

`bundle update --group {{nom_groupe}}`

- Liste les gem(s) installée(s) dans le `Gemfile` avec les nouvelles versions disponibles :

`bundle outdated`

- Crée un nouveau squelette de gem :

`bundle gem {{nom_de_la_gem}}`
