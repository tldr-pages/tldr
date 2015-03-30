#git remote

> Manage set of tracked repositories (“remotes”)

- Show a list of existing remotes, their names and URL

`git remote -v`

- Add a remote

`git remote add {{remote_name}} {{remote_url}}`

- Add a remote and run fetch on it

`git remote add -f {{remote_name}} {{remote_url}}`

- Remove a remote

`git remote remove {{remote_name}}`

- Rename a remote

`git remote rename {{old_name}} {{new_name}}`
