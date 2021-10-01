# cvs

> Concurrent Versions System, a revision control system
> More information: <http://cvs.nongnu.org>.

- Create repository (need to manually set CVSROOT to /path/to/repo in .bashrc)

`cvs -d /path/to/repo init`

- Add project to repository. Navigate to project folder and run

`cvs import -m "message" projectname version vendor`

- Checkout a project

`cvs checkout projectname`

- Check file diff/changes

`cvs diff file.txt`

- Add a file

`cvs add file.txt`

- Commit a file

`cvs commit -m "commit message" file.txt`

- Update working directory from repository

`cvs update`
