# tcsh

> C shell with file name completion and command line editing.
> More information: <https://linux.die.net/man/1/tcsh>.

- Start an interactive shell session:

`tcsh`

- Start an interactive shell session without loading startup configs:

`tcsh -f`

- Execute a [c]ommand and then exit:

`tcsh -c "{{command}}"`

- Execute a script and then exit:

`tcsh {{path/to/script.tcsh}}`

- Check a script for syntax errors and then exit:

`tcsh -n {{path/to/script.tcsh}}`

- Print a version and then exit:

`tcsh --version`
