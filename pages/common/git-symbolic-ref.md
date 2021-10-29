# git symbolic-ref

> Read, change, or delete files that store references.
> More information: <https://git-scm.com/docs/git-symbolic-ref>.

- Store a reference by a name:

`git symbolic-ref refs/{{name}} {{ref}}`

- Store a reference by name, including a message with a reason for the update:

`git symbolic-ref -m "{{message}}" refs/{{name}} refs/heads/{{branch_name}}`

- Read a reference by name:

`git symbolic-ref refs/{{name}}`

- Delete a reference by name:

`git symbolic-ref --delete refs/{{name}}`

- For scripting, hide errors with `--quiet` and use `--short` to simplify ("refs/heads/X" prints as "X"):

`git symbolic-ref --quiet --short refs/{{name}}`
