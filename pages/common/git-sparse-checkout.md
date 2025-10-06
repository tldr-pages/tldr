# git sparse-checkout

> Lets you check out only part of a repository’s files — instead of cloning or checking out everything.
> More information: <https://manned.org/git-sparse-checkout>.

- Enable sparse checkout:

`git sparse-checkout init`

- Disable sparse-checkout and restore full repository:

`git sparse-checkout disable`

- Specify which directories (or files) to include:

`git sparse-checkout set {{path/to/folder1}}`

- Add more paths later:

`git sparse-checkout add {{path/to/folder2}}`
