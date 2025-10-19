# git-merge-index

> Run a merge program on files that need merging.
> More information: <https://git-scm.com/docs/git-merge-index>.

- Merge all files needing resolution using the standard helper:

`git merge-index git-merge-one-file -a`

- Merge a specific file:

`git merge-index git-merge-one-file -- {{path/to/file}}`

- Merge multiple files, continuing on failures:

`git merge-index -o git-merge-one-file -- {{path/to/file1 path/to/file2 ...}}`

- Quietly merge all files with a custom program:

`git merge-index -q {{merge-program}} -a`

- Inspect merge inputs for a file using cat:

`git merge-index cat -- {{path}}`
