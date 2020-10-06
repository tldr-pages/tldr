# git subtree

> Tool to manage project dependencies as subprojects.
> More information: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>.

- Add a git repository as a subtree:

`git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{main}}`

- Update subtree repository to its latest commit:

`git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{main}}`

- Merge a subtree repository into main:

`git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{main}}`

- Push commits to a subtree repository:

`git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{main}}`

- Extract a new project history from the history of a subtree:

`git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}`
