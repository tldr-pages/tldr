# git symbolic-ref

> Read, change or delete files that store references.
> More information: <https://git-scm.com/docs/git-symbolic-ref>.

- Store a reference by a name (that preferably begins with "ref/"):

`git symbolic-ref {{name}} {{ref}}`

- Store a reference by name, including a message with a reason for the update:

`git symbolic-ref -m "Automated deploy" refs/production refs/heads/main`

- Read a reference by name:

`git symbolic-ref {{name}}`

- Delete a reference by name (name must begin with ref/):

`git symbolic-ref --delete {{name}}`

- For scripting, hide errors with --quiet and use --short to simplify ("refs/heads/X" prints as "X"):

`git symbolic-ref --quiet --short {{name}}`
