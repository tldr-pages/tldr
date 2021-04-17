# entr

> Run arbitrary commands when files change.
> More information: <https://manned.org/entr>.

- Rebuild with `make` if any file in any subdirectory changes:

`{{ag -l}} | entr {{make}}`

- Rebuild and test with `make` if any `.c` source files in the current directory change:

`{{ls *.c}} | entr {{'make && make test'}}`

- Send a `SIGTERM` to any previously spawned ruby subprocesses before executing `ruby main.rb`:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- Run a command with the changed file (`/_`) as an argument:

`{{ls *.sql}} | entr {{psql -f}} /_`
