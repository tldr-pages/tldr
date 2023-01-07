# dart

> Ligne de commande pour gérer un projet Dart.
> Plus d'informations : <https://dart.dev/tools/dart-tool>.

- Initialise un nouveau projet Dart dans un dossier du même nom :

`dart create {{nom_du_projet}}`

- Exécuter un fichier Dart :

`dart run {{chemin/vers/fichier.dart}}`

- Télécharger les dépendences pour le projet courant :

`dart pub get`

- Exécuter les tests unitaire pour le projet courant :

`dart test`

- Mettre à jour les dépendances d'un projet pour supporter null-safety :

`dart pun upgrade --null-safety`

- Compiler un fichier Dart vers un binaire natif :

`dart compile exe {{chemin/vers/fichier.dart}}`
