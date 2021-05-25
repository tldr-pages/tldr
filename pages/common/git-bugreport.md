# git bugreport

> Captures debug information from the system and user, generating a text file to aid in the reporting of a bug in Git.
> More information: <https://git-scm.com/docs/git-bugreport>.

- Create a new bugreport file in the current directory:

`git bugreport`

- Create a new bugreport file in the specified directory, creating it if it does not exist:

`git bugreport --output-directory {{path/to/directory}}`

- Create a new bugreport file with the specified filename suffix in `strftime` format:

`git bugreport --suffix {{%m%d%y}}`
