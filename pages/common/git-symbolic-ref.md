# git symbolic-ref

> Read, change or delete files that store references.
> More information: <https://git-scm.com/docs/git-symbolic-ref>.

- Write to {{name}} (should begin with `ref/`), with ref preferably being a valid reference or commitish:

`git symbolic-ref {{name}} {{ref}}`

- Write, including a message with a reason for the update:

`git symbolic-ref -m "Automated deploy" refs/production refs/heads/main`

- Read (complains if the read {{ref}} is not a valid reference within the repository):

`git symbolic-ref {{name}}`

- Delete (-m not allowed, name must begin with ref/):

`git symbolic-ref --delete {{name}}`

- For scripting add --quiet to hide error outputs, and --short to simplify (typically hiding "refs/heads/") when returning a read {{name}}:

`git symbolic-ref --quiet --short {{nam}}`
