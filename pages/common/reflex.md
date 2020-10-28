# reflex

> Reflex is a small tool to watch a directory and rerun a command when certain files change.
> More information: <https://github.com/cespare/reflex>.

- Rebuild with `make` if any file changes:

`reflex make`

- Compile and run Go application if any .go file changes:

`reflex -r '\.go$' go run .`

- Ignore a directory when wahtcing for changes:

`reflex -R '^node_modules/' yarn test`

- Run command when reflex starts and restarts on file changes:

`reflex -s go test`

- Substitude what file changes:

`reflex -- echo {}`
