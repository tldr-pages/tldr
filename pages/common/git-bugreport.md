# git bugreport

> Captures information about the user's machine, Git client, and repository state, as well as a form requesting information about the behavior the user observed, into a single text file which the user can then share, for example to the Git mailing list, in order to report an observed bug.

- Create a new bugreport file in the current directory:

`git bugreport`

- Create a new bugreport file in the specified, creating the directory if it does not exist:

`git bugreport --output-directory {{path/to/directory}}`

- Create a new bugreport file with the filename suffix in the specified `strftime` format:

`git bugreport --suffix {{%m%d%y}}`
