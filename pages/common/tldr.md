# tldr

> Display simple help pages for command-line tools from the tldr-pages project.
> Note: The `--language` and `--list` options are not required by the client specification, but most clients implement them.
> More information: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Print the tldr page for a specific command (hint: this is how you got here!):

`tldr {{command}}`

- Print the tldr page for a specific subcommand:

`tldr {{command}} {{subcommand}}`

- Print the tldr page for a command in the given language (if available, otherwise fall back to English):

`tldr {{[-L|--language]}} {{language_code}} {{command}}`

- Print the tldr page for a command from a specific platform:

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{command}}`

- Update the local cache of tldr pages:

`tldr {{[-u|--update]}}`

- List all pages for the current platform and `common`:

`tldr {{[-l|--list]}}`

- List all available subcommand pages for a command:

`tldr {{[-l|--list]}} | grep {{command}} | column`

- Print the tldr page for a random command:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
