10.# boxxy

> Redirect file locations for programs that don't respect the XDG standards.
> More information: <https://github.com/queer/boxxy>.

- Run a program with file redirections defined in `~/.config/boxxy/boxxy.yaml`:

`boxxy {{program}}`

- Scan your home directory for rule suggestions:

`boxxy scan`

- Trace what files a program touches and save a report in `boxxy-report.txt` in the current directory:

`boxxy {{[-t|--trace]}} {{program}}`

- Pass a redirection rule directly on the terminal:

`boxxy {{[-r|--rule]}} {{path/to/file_or_directory}}:{{path/to/redirection}}:{{file|directory}} {{program}}`

- View the config file:

`boxxy config`

- Display help:

`boxxy -h`
