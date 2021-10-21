# jest

> Une plateforme de test JavaScript sans configuration.
> Plus d'informations : <https://jestjs.io>.

- Exécuter tous les tests disponibles :

`jest`

- Exécuter les suites de test de fichiers donnés :

`jest {{chemin/vers/fichier1}} {{chemin/vers/fichier2}}`

- Exécuter les suites de test pour des fichiers, dans le répertoire courant et ses sous-répertoires, dont le chemin correspond à l'expression régulière indiquée :

`jest {{expression_régulière}} {{expression_régulière}}`

- Exécuter les tests dont les noms correspondent aux expressions régulières indiquées :

`jest --testNamePattern {{nom_test}}`

- Exécuter les suites de test associées à un fichier source donné :

`jest --findRelatedTests {{chemin/vers/fichier_source.js}}`

- Exécuter les suites de test associées à tous les fichiers non commités :

`jest --onlyChanged`

- Surveiller les changements sur les fichiers et ré-exécuter les tests associés :

`jest --watch`

- Montrer l'aide :

`jest --help`
