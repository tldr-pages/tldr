# git archive

> Create an archive of files from a named tree.
> More information: <https://git-scm.com/docs/git-archive>.

- Create a tar archive from the contents of the current HEAD and print it to standard output:

`git archive --verbose HEAD`

- Create a zip archive from the current HEAD and print it to standard output:

`git archive --verbose --format=zip HEAD`

- Same as above, but write the zip archive to file:

`git archive --verbose --output={{target.zip}} HEAD`

- Create a tar archive from the contents of the latest commit on the current branch:

`git archive --verbose --output={{target.tar}} HEAD`

- Create a tar archive from the contents of a specific directory:

`git archive --output={{target.tar}} HEAD:{{directory}}`

- Same as above, but change the prefix of all files in the archive:

`git archive --output={{target.tar}} --prefix={{prefix}} HEAD:{{directory}}`
