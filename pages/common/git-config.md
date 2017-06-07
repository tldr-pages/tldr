# git config

> Manage custom configuration options for git repositories.
> These configurations can be local (for the current repository) or global (for the current user).

- List only local configurations (stored in `.git/config` in the current repository):

`git config --list --local`

- List only global configurations (stored in `~/.gitconfig`):

`git config --list --global`

- List all configurations that have been defined either locally or globally:

`git config --list`

- Get the local value of a given configuration entry:

`git config alias.unstage`

- Set the global value of a given configuration entry:

`git config --global alias.unstage "reset HEAD --"`

- Unset a global configuration entry (reverts to git's default behavior):

`git config --global --unset alias.unstage`
