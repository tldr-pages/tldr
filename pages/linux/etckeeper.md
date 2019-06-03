# etckeeper

> Track system configuration files in git.
> More information: http://etckeeper.branchable.com/.

- Initialize: Run once from /etc to initialize a new repo, and add package manager hooks for automatic commits when installing and removing packages:

`sudo etckeeper init`

- Commit all changes in /etc:

`sudo etckeeper commit {{message}}`

- Run arbitrary git commands:

`sudo etckeeper vcs {{command}}`

- Check if there are uncommitted changes:

`if (sudo etckeeper unclean); then echo dirty; else echo clean; fi`

- Destroy existing repo and stop tracking changes:

`sudo etckeeper uninit`
