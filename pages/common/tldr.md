# tldr

> Display simple help pages for command-line tools from the tldr-pages project.
> Different tldr clients do not have the full specification of features, therefore some of these commands may not be accessible to your client.
> More information: <https://tldr.sh>.

- Print the tldr page for a specific command (hint: this is how you got here!):

`tldr {{command}}`

- Print the tldr page for a specific subcommand:

`tldr {{command}}-{{subcommand}}`

- Print the tldr page for a command for a specific platform:

`tldr {{-p|--platform}} {{android|linux|osx|sunos|windows}} {{command}}`

- Print the tldr page for a command in a specific language:

`tldr {{-l|--language}} {{ru}} {{command}}`

- Update local pages:

`tldr {{-u|--update}}`
