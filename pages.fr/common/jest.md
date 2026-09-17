# jest

> Une plateforme de test JavaScript sans configuration.
> Plus d'informations : <https://jestjs.io/docs/cli>.

- Exécuter tous les tests disponibles :

`jest`

- Exécuter les suites de test de fichiers donnés :

`jest {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Exécuter les suites de test pour des fichiers, dans le répertoire courant et ses sous-répertoires, dont le chemin correspond à la `regex` indiquée :

`jest {{regex1 regex2 ...}}`

- Exécuter les tests dont les noms correspondent aux `regex` indiquées :

`jest --testNamePattern {{regex}}`

- Exécuter les suites de test associées à un fichier source donné :

`jest --findRelatedTests {{chemin/vers/fichier_source.js}}`

- Exécuter les suites de test associées à tous les fichiers non commités :

`jest --onlyChanged`

- Surveiller les changements sur les fichiers et ré-exécuter les tests associés :

`jest --watch`

- Montrer l'aide :

`jest --help`
