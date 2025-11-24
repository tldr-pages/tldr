# fossil

> Distributed version control system.
> Some subcommands such as `commit` have their own usage documentation.
> More information: <https://fossil-scm.org/home/help>.

- Initialize a new repository:

`fossil init {{path/to/repository.fossil}}`

- Clone an existing repository:

`fossil clone {{url}} {{path/to/repository.fossil}}`

- Open a working directory from a repository:

`fossil open {{path/to/repository.fossil}}`

- Add a file to the repository:

`fossil add {{path/to/file}}`

- Commit changes:

`fossil commit -m "{{message}}"`

- Sync with the remote:

`fossil sync`

- Show repository status:

`fossil status`

- Start the built-in web interface:

`fossil ui`
