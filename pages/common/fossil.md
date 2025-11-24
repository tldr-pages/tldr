# fossil

> Distributed version control system with a built-in wiki, issue tracker, and web interface.
> More information: <https://fossil-scm.org>.

- Initialize a new Fossil repository:

`fossil init {{path/to/repository.fossil}}`

- Clone an existing repository:

`fossil clone {{https://example.com/repo.fossil}} {{path/to/local.fossil}}`

- Open a working directory from a repository file:

`fossil open {{path/to/repository.fossil}}`

- Add a file to version control:

`fossil add {{path/to/file}}`

- Commit changes with a message:

`fossil commit -m "{{message}}"`

- Synchronize with the remote server:

`fossil sync`

- View the web interface in a browser:

`fossil ui`

- Show the current status:

`fossil status`
