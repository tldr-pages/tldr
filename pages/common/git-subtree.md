# git subtree

> Merge subtrees together or split repository into subtrees.
> More information: <https://manned.org/git-subtree>.

- Add a Git repository as a subtree and squash the commits together:

`git subtree add {{[-P|--prefix]}} {{path/to/directory}} --squash {{repository_url}} {{branch_name}}`

- Update subtree repository to its latest commit:

`git subtree pull {{[-P|--prefix]}} {{path/to/directory}} {{repository_url}} {{branch_name}}`

- Merge recent changes up to the latest subtree commit into the subtree:

`git subtree merge {{[-P|--prefix]}} {{path/to/directory}} --squash {{repository_url}} {{branch_name}}`

- Push commits to a subtree repository:

`git subtree push {{[-P|--prefix]}} {{path/to/directory}} {{repository_url}} {{branch_name}}`

- Extract a new project history from the history of a subtree:

`git subtree split {{[-P|--prefix]}} {{path/to/directory}} {{repository_url}} {{[-b|--branch]}} {{branch_name}}`
