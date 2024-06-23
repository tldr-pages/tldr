# tldr

> Display simple help pages for command-line tools from the tldr-pages project.
> Note: the `--language` and `--list` options are not required by the client specification, but most clients implement them.
> More information: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Print the tldr page for a specific command (hint: this is how you got here!):

`tldr {{command}}`

- Print the tldr page for a specific subcommand:

`tldr {{command}} {{subcommand}}`

- Print the tldr page for a command in the given [L]anguage (if available, otherwise fall back to English):

`tldr --language {{language_code}} {{command}}`

- Print the tldr page for a command from a specific [p]latform:

`tldr --platform {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{command}}`

- [u]pdate the local cache of tldr pages:

`tldr --update`

- [l]ist all pages for the current platform and `common`:

`tldr --list`
