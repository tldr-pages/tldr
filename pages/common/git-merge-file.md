# git merge-file

> Run a three-way merge on a single file.
> See also: `git merge`, `git merge-tree`.
> More information: <https://git-scm.com/docs/git-merge-file>.

- Merge the changes from a base file to another file into the current file (modifies the current file in place):

`git merge-file {{path/to/current_file}} {{path/to/base_file}} {{path/to/other_file}}`

- Print the merge result to `stdout` instead of modifying the current file:

`git merge-file {{[-p|--stdout]}} {{path/to/current_file}} {{path/to/base_file}} {{path/to/other_file}}`

- Resolve conflicts by using the version from the current file:

`git merge-file --ours {{path/to/current_file}} {{path/to/base_file}} {{path/to/other_file}}`

- Resolve conflicts by using the version from the other file:

`git merge-file --theirs {{path/to/current_file}} {{path/to/base_file}} {{path/to/other_file}}`

- Resolve conflicts by keeping the lines from both files:

`git merge-file --union {{path/to/current_file}} {{path/to/base_file}} {{path/to/other_file}}`

- Include the base version in conflict markers and use custom labels for each file:

`git merge-file --diff3 -L {{current_label}} -L {{base_label}} -L {{other_label}} {{path/to/current_file}} {{path/to/base_file}} {{path/to/other_file}}`
