# git cvsimport

> Import a CVS repository into Git.
> More information: <https://git-scm.com/docs/git-cvsimport>.

- Import a CVS module into a Git repository:

`git cvsimport -C {{path/to/git/repository}} {{module_name}}`

- Import from a specific CVS root:

`git cvsimport -d {{:pserver:user@host:/path/to/cvsroot}} -C {{path/to/git/repository}} {{module_name}}`

- Import and specify the remote name for tracking:

`git cvsimport -o {{origin}} -C {{path/to/git/repository}} {{module_name}}`

- Import from a specific date onwards:

`git cvsimport -d {{:pserver:user@host:/path/to/cvsroot}} -C {{path/to/git/repository}} -s {{2020-01-01}} {{module_name}}`

- Display help:

`git cvsimport --help`
