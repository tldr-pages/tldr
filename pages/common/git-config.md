# git config

> Manage custom configuration options for Git repositories.
> These configurations can be local (for the current repository) or global (for the current user).
> More information: <https://git-scm.com/docs/git-config>.

- List only local configuration entries (stored in `.git/config` in the current repository):

`git config --list --local`

- List only global configuration entries (stored in `~/.gitconfig` by default or in `$XDG_CONFIG_HOME/git/config` if such a file exists):

`git config --list --global`

- List only system configuration entries (stored in `/etc/gitconfig`), and show their file location:

`git config --list --system --show-origin`

- Get the value of a given configuration entry:

`git config alias.unstage`

- Set the global value of a given configuration entry:

`git config --global alias.unstage "reset HEAD --"`

- Revert a global configuration entry to its default value:

`git config --global --unset alias.unstage`

- Edit the Git configuration for the current repository in the default editor:

`git config --edit`

- Edit the global Git configuration in the default editor:

`git config --global --edit`
