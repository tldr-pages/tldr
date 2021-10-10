# git symbolic-ref

> Read, change or delete named references.
> For a longer description (and why "symbolic"), see <https://git-scm.com/docs/git-symbolic-ref>.

- Write (name should begin with `ref/` and ref can be any string but is meant to be a valid reference - or commitish):

`git symbolic-ref {{name}} {{ref}}`

- Write, including a message with a reason for the update:

`git symbolic-ref -m "Automated deploy" refs/production refs/heads/main`

- Read (complains if the read {{ref}} is not a valid reference within the repo):

`git symbolic-ref {{name}}`

- Read, with --short to shorten the output, removing refs/heads/:

`git symbolic-ref --short refs/production`

- Delete (-m not allowed, name must begin with ref/):

`git symbolic-ref --delete {{name}}`

- For scripting usage add --quiet to replace error output with a non-zero exit code if {{ref}} does not exist:

`git symbolic-ref --quiet ref/production HEAD`
