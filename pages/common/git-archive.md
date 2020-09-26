# git archive

> Create an archive of files from a named tree.
> More information: <https://git-scm.com/docs/git-archive>.

- Create a tar archive from the contents of the latest commit on the current branch:

`git archive --verbose -o {{target.tar}} HEAD`

- Create a tar archive from the contents of a specific directory:

`git archive -o {{target.tar}} HEAD:{{directory}}`

- Same as above, but change the prefix of all files in the archive:

`git archive -o {{target.tar}} --prefix={{prefix}} HEAD:{{directory}}`

- Create a zip archive from the latest commit and print it to standard output:

`git archive --format=zip HEAD`

- Create a zip archive from the latest commit on a specific branch:

`git archive -o {{target.zip}} {{branch_name}}`
