# git describe

> Give an object a human readable name based on an available ref.
> More information: <https://git-scm.com/docs/git-describe>.

- Create a unique name for the current commit (the name contains the most recent annotated tag, the number of additional commits, and the abbreviated commit hash):

`git describe`

- Create a name with 4 digits for the abbreviated commit hash:

`git describe --abbrev={{4}}`

- Generate a name with the tag reference path:

`git describe --all`

- Describe a git tag:

`git describe {{v1.0.0}}`

- Create a name for the last commit of a given branch:

`git describe {{branch_name}}`
