# go

> Outil de gestion du code source Go.
> Certaines sous-commandes telles que `build` ont leur propre documentation d'utilisation.
> Plus d'informations : <https://pkg.go.dev/cmd/go>.

- Télécharge et installe un paquet, spécifié par son chemin d'importation :

`go get {{chemin_du_paquet}}`

- Compile et exécute un fichier source (il doit contenir un paquet `main`) :

`go run {{fichier}}.go`

- Compile un fichier source dans un exécutable nommé :

`go build -o {{executable}} {{fichier}}.go`

- Compile le paquet présent dans le répertoire courant :

`go build`

- Exécute tous les cas de test du paquet courant (les fichiers doivent se terminer par `_test.go`) :

`go test`

- Compile et installe le paquet actuel :

`go install`

- Initialise un nouveau module dans le répertoire courant :

`go mod init {{nom_du_module}}`
