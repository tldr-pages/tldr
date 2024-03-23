# entr

> Run arbitrary commands when files change.
> More information: <http://eradman.com/entrproject/>.

- Rebuild with `make` if any file in any subdirectory changes:

`{{ag -l}} | entr {{make}}`

- Rebuild and test with `make` if any `.c` source files in the current directory change:

`{{ls *.c}} | entr {{'make && make test'}}`

- Send a `SIGTERM` to any previously spawned ruby subprocesses before executing `ruby main.rb`:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- Run a command with the changed file (`/_`) as an argument:

`{{ls *.sql}} | entr {{psql -f}} /_`

- [c]lear the screen and run a query after the SQL script is updated:

`{{echo my.sql}} | entr -cp {{psql -f}} /_`

- Rebuild the project if source files change, limiting output to the first few lines:

`{{find src/}} | entr -s {{'make | sed 10q'}}`

- Launch and auto-[r]eload a Node.js server:

`{{ls *.js}} | entr -r {{node app.js}}`
