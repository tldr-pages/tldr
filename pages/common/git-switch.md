# git switch

> Switch between git branches. Requires git version 2.23+.
> See also `git checkout`.
> More information: <https://git-scm.com/docs/git-switch/>.

- Switch to an existing branch:

`git switch {{branch_name}}`

- Create a new branch and switch to it:

`git switch --create {{branch_name}}`

- Create a new branch based on an existing commit:

`git switch --create {{branch_name}} {{commit}}`

- Update all submodules to match the target branch:

`git switch --recurse-submodules {{branch_name}}`

- Automatically merge the current branch and any uncommitted changes into the new branch:

`git switch --merge {{branch_name}}`
