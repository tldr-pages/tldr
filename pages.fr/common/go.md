# go

> Outil de gestion du code source Go.
> Certaines sous-commandes telles que `go build` ont leur propre documentation d'utilisation.
> Plus d'informations : <https://golang.org>.

- Télécharger et installer un paquet, spécifié par son chemin d'importation :

`go get {{chemin_du_paquet}}`

- Compiler et exécuter un fichier source (il doit contenir un paquet `main`) :

`go run {{fichier}}.go`

- Compiler un fichier source dans un exécutable nommé :

`go build -o {{executable}} {{fichier}}.go`

- Compile le paquet présent dans le répertoire courant :

`go build`

- Exécuter tous les cas de test du paquet courant (les fichiers doivent se terminer par `_test.go`) :

`go test`

- Compiler et installer le paquet actuel :

`go install`

- Initialiser un nouveau module dans le répertoire courant :

`go mod init {{nom_du_module}}`
