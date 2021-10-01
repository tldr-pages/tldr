# cvs

> Concurrent Versions System, a revision control system.
> More information: <http://cvs.nongnu.org>.

- Create repository (need to manually set CVSROOT to /path/to/repo in .bashrc):

`cvs -d {{path/to/repo}} init`

- Add project to repository. Navigate to project folder and run:

`cvs import -m "{{message}}" {{project_name}} {{version}} {{vendor}}`

- Checkout a project:

`cvs checkout {{project_name}}`

- Check file diff/changes:

`cvs diff {{path/to/file}}`

- Add a file:

`cvs add {{path/to/file}}`

- Commit a file:

`cvs commit -m "{{message}}" {{path/to/file}}`

- Update working directory from repository:

`cvs update`
