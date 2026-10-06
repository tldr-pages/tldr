# jest

> Une plateforme de test JavaScript sans configuration.
> Plus d'informations : <https://jestjs.io/docs/cli>.

- Exécute tous les tests disponibles :

`jest`

- Exécute les suites de test de fichiers donnés :

`jest {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Exécute les suites de test pour des fichiers, dans le répertoire actuel et ses sous-répertoires, dont le chemin correspond à la `regex` indiquée :

`jest {{regex1 regex2 ...}}`

- Exécute les tests dont les noms correspondent aux `regex` indiquées :

`jest --testNamePattern {{regex}}`

- Exécute les suites de test associées à un fichier source donné :

`jest --findRelatedTests {{chemin/vers/fichier_source.js}}`

- Exécute les suites de test associées à tous les fichiers non commités :

`jest --onlyChanged`

- Surveille les changements sur les fichiers et ré-exécute les tests associés :

`jest --watch`

- Affiche l'aide :

`jest --help`
