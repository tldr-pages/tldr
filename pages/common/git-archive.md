# git archive

> Create an archive of files from a tree.
> More information: <https://git-scm.com/docs/git-archive>.

- Create a tar archive from the contents of the current HEAD and print it to `stdout`:

`git archive --verbose HEAD`

- Use the Zip format and report progress [v]erbosely:

`git archive {{-v|--verbose}} --format zip HEAD`

- [o]utput the Zip archive to a specific file:

`git archive -v {{-o|--output}} {{path/to/file.zip}} HEAD`

- Create a tar archive from the contents of the latest commit of a specific branch:

`git archive -o {{path/to/file.tar}} {{branch_name}}`

- Use the contents of a specific directory:

`git archive -o {{path/to/file.tar}} HEAD:{{path/to/directory}}`

- Prepend a path to each file to archive it inside a specific directory:

`git archive -o {{path/to/file.tar}} --prefix {{path/to/prepend}}/ HEAD`
