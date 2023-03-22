# mcfly

> A smart command history search and management tool.
> Replaces your default shell history search (ctrl-r) with an intelligent search engine providing context and relevance to the commands.
> More information: <https://github.com/cantino/mcfly>.

- Print the mcfly integration code for the specified shell:

`mcfly init {{bash|fish|zsh}}`

- Search the history for a command, with 20 results:

`mcfly search --results {{20}} "{{search_terms}}"`

- Add a new command to the history:

`mcfly add "{{command}}"`

- Record that a directory has moved and transfer the historical records from the old path to the new one:

`mcfly move "{{path/to/old_directory}}" "{{path/to/new_directory}}"`

- Train the suggestion engine (developer tool):

`mcfly train`

- Display help for a specific subcommand:

`mcfly help {{subcommand}}`
