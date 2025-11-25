# fossil

> Distributed version control system with a built-in wiki, bug tracker, and web interface.
> Some subcommands such as `commit` have their own usage documentation.
> More information: <https://fossil-scm.org/home/help>.

- Initialize a new empty Fossil repository:

`fossil init {{repository_name.fossil}}`

- Create a local copy of a remote repository:

`fossil clone {{remote_url}} {{repository_name.fossil}}`

- Show an overview of the current repository state:

`fossil status`

- Stage a new file:

`fossil add {{path/to/file}}`

- Stage a file for removal:

`fossil {{[rm|delete]}} {{path/to/file}}`

- Check in all staged changes:

`fossil {{[ci|commit]}} {{[-m|--comment]}} "{{comment}}"`

- Push changes from the local repository to a remote repository:

`fossil push {{remote_url}}`

- Pull changes from a remote repository into the local repository:

`fossil pull {{remote_url}}`
