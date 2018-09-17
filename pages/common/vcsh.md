# vcsh

> Version Control System for $HOME - multiple Git repositories in $HOME.

- Execute git command on managed repository:

`vcsh {{repository_name}} {{git_command}}`

- Initialize (empty) repository:

`vcsh init {{repository_name}}`

- Clone repository into custom name:

`vcsh clone {{git_url}} {{repository_name}}`

- List all managed repositories:

`vcsh list`

- Pull/pull all managed repositories from/to remotes:

`vcsh {{push|pull}}`

- Write custom .gitignore file for managed repository: 

`vcsh write-gitignore {{repository_name}}`
