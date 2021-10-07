# cvs

> Concurrent Versions System, a revision control system.
> More information: <https://cvs.nongnu.org>.

- Create a new repository (requires the `CVSROOT` environment variable to be set externally):

`cvs -d {{path/to/repository}} init`

- Add a project to the repository:

`cvs import -m "{{message}}" {{project_name}} {{version}} {{vendor}}`

- Checkout a project:

`cvs checkout {{project_name}}`

- Show changes made to files:

`cvs diff {{path/to/file}}`

- Add a file:

`cvs add {{path/to/file}}`

- Commit a file:

`cvs commit -m "{{message}}" {{path/to/file}}`

- Update the working directory from the remote repository:

`cvs update`
