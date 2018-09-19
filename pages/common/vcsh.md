# vcsh

> Version Control System for your home directory using git repositories.

- Initialize (empty) repository:

`vcsh init {{repository_name}}`

- Clone repository into custom name:

`vcsh clone {{git_url}} {{repository_name}}`

- List all managed repositories:

`vcsh list`

- Execute git command on managed repository:

`vcsh {{repository_name}} {{git_command}}`

- Push/pull all managed repositories to/from remotes:

`vcsh {{push|pull}}`

- Write custom .gitignore file for managed repository:

`vcsh write-gitignore {{repository_name}}`
