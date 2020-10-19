# git config

> Manage custom configuration options for git repositories.
> These configurations can be local (for the current repository) or global (for the current user).
> More information: <https://git-scm.com/docs/git-config>.

- List only local configuration entries (stored in `.git/config` in the current repository):

`git config --list --local`

- List only global configuration entries (stored in `~/.gitconfig`):

`git config --list --global`

- List all configuration entries that have been defined either locally or globally:

`git config --list`

- Get the value of a given configuration entry:

`git config alias.unstage`

- Set the global value of a given configuration entry:

`git config --global alias.unstage "reset HEAD --"`

- Revert a global configuration entry to its default value:

`git config --global --unset alias.unstage`

- Edit the git configuration for the current repository in the default editor:

`git config --edit`

- Edit the global git configuration in the default editor:

`git config --global --edit`
