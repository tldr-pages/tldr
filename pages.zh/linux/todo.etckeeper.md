# etckeeper

> Track system configuration files in git.
> More information: <http://etckeeper.branchable.com/>.

- Set up a git repo and perform various setup tasks (run from /etc):

`sudo etckeeper init`

- Commit all changes in /etc:

`sudo etckeeper commit {{message}}`

- Run arbitrary git commands:

`sudo etckeeper vcs {{status}}`

- Check if there are uncommitted changes (only returns an exit code):

`sudo etckeeper unclean`

- Destroy existing repo and stop tracking changes:

`sudo etckeeper uninit`
