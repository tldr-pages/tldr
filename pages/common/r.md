# R

> R language interpreter.
> More information: <https://manned.org/R>.

- Start a REPL (interactive shell):

`R`

- Start R in vanilla mode (i.e. a blank session that doesn't save the workspace at the end):

`R --vanilla`

- Execute a file:

`R {{[-f|--file]}} {{path/to/file.R}}`

- Execute an R expression and then exit:

`R -e {{expr}}`

- Run R with a debugger:

`R {{[-d|--debugger]}} {{debugger}}`

- Check R packages from package sources:

`R CMD check {{path/to/package_source}}`

- Display version:

`R --version`
