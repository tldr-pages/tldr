# tldr

> Display simple help pages for command-line tools from the tldr-pages project.
> More information: <https://tldr.sh>.

- Print a tldr page for a specific command (hint: this is how you got here!):

`tldr {{cd}}`

- Print a tldr page for a command for a specific platform:

`tldr --platform {{android|linux|osx|sunos|windows}} {{cd}}`

- Print a tldr page for a command in a specific language (client may not support this option):

`tldr --language {{ru}} {{cd}}`

- Print a tldr page for a specific subcommand:

`tldr {{git}}-{{checkout}}`

- Update local pages (client may not support caching with this option):

`tldr --update`
