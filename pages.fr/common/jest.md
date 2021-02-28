# jest

> Une plateforme de test JavaScript avec zero configuration.
> Plus d'informations : <https://jestjs.io>.

- Exécuter tous les tests disponibles :

`jest`

- Exécuter les suites de test des fichiers dont les chemins correspondent aux expressions régulières indiquées :

`jest {{fichier_test1}} {{chemin/vers/fichier_test2.js}}`

- Exécuter les tests dont les noms correspondent aux expressions régulières indiquées :

`jest --testNamePattern {{nom_test}}`

- Exécuter les suites de test associées à un fichier source donné :

`jest --findRelatedTests {{chemin/vers/fichier_source.js}}`

- Exécuter les suites de test associées à tous les fichiers non commités :

`jest --onlyChanged`

- Surveiller les changements sur les fichiers et réexécuter les tests associés :

`jest --watch`

- Montrer l'aide :

`jest --help`
