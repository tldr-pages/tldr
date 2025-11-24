# fossil

> A distributed version control system supporting bug tracking, wiki, and a built-in web interface—all in a single file.
> More information: <https://fossil-scm.org/>.

- Initialize a new repository file:
`fossil init {{path/to/repository.fossil}}`

- Clone a remote repository:
`fossil clone {{url}} {{path/to/repository.fossil}}`

- Open a working directory from a repository file:
`fossil open {{path/to/repository.fossil}}`

- Show the status of the working directory:
`fossil status`

- Add a file or directory to version control:
`fossil add {{path/to/file_or_directory}}`

- Commit changes with a message:
`fossil commit -m "{{message}}"`

- View the commit history:
`fossil timeline`

- Sync local changes with the remote:
`fossil sync`

- Launch the built-in web UI:
`fossil ui`
