# git config

> Manage custom configuration options for Git repositories.
> These configurations can be local (for the current repository) or global (for the current user).
> More information: <https://git-scm.com/docs/git-config>.

- Globally set your name or email (this information is required to commit to a repository and will be included in all commits):

`git config --global {{user.name|user.email}} "{{Your Name|email@example.com}}"`

- List local or global configuration entries:

`git config --list --{{local|global}}`

- List only system configuration entries (stored in `/etc/gitconfig`), and show their file location:

`git config --list --system --show-origin`

- Get the value of a given configuration entry:

`git config alias.unstage`

- Set the global value of a given configuration entry:

`git config --global alias.unstage "reset HEAD --"`

- Revert a global configuration entry to its default value:

`git config --global --unset alias.unstage`

- Edit the local Git configuration (`.git/config`) in the default editor:

`git config --edit`

- Edit the global Git configuration (`~/.gitconfig` by default or `$XDG_CONFIG_HOME/git/config` if such a file exists) in the default editor:

`git config --global --edit`
