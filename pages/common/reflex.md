# reflex

> Reflex is a small tool to watch a directory and rerun a command when certain files change.
> More information: <https://github.com/cespare/reflex>.

- Rebuild with `make` if any file changes:

`reflex make`

- Compile and run Go application if any .go file changes:

`reflex -r '{{\.go$}}' {{go run .}}`

- Ignore a directory when watching for changes:

`reflex -R '{{^dir/}}' {{command}}`

- Run command when reflex starts and restarts on file changes:

`reflex --start-service=true {{command}}`

- Substitude what file changes:

`reflex -- echo {}`
