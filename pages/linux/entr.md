# entr

> Run arbitrary commands when files change.

- Rebuild with `make` if any files in any subfolders change:

`ag -l | entr make`

- Rebuild and test with `make` if any `.c` source files in the current directory change:

`ls *.c | entr 'make && make test'`

- Reload the MuPDF viewer whenever the source `.pdf` changes:

`ls *.pdf | entr pkill -HUP mupdf`

- Reload the spawned childprocess with `SIGTERM` before restarting:

`ls *.rb | entr -r ruby main.rb`

- Run a command with the changed file (`/_`) as input:

`ls *.sql | entr psql -f /_`
