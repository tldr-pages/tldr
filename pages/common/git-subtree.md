# git subtree

> Tool to manage project dependencies as subprojects.
> More information: <https://manned.org/git-subtree.1>.

- Add a Git repository as a subtree:

`git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- Update subtree repository to its latest commit:

`git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- Merge recent changes up to the latest subtree commit into the subtree:

`git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- Push commits to a subtree repository:

`git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- Extract a new project history from the history of a subtree:

`git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}`
