# jj

> Jujutsu: a Git-compatible version control system.
> Uses a stageless, change-based model; interoperates with Git via `jj git`.
> More information: <https://jj-vcs.github.io/jj/latest/>.

- Initialize a colocated Jujutsu repository in the current Git project:

`jj git init --colocate`

- Show the working copy status and the current `@` change:

`jj status`

- Create a new change on top of the current one with a message:

`jj new -m "{{short_description}}"`

- Amend the current change's description:

`jj describe -m "{{updated_message}}"`

- View recent history (last 20 changes):

`jj log -n {{20}}`

- Create (or move) a bookmark (branch-like pointer) to the current change:

`jj bookmark set {{bookmark_name}}`

- Push changes and bookmarks to the default Git remote (allow creating new bookmarks):

`jj git push --allow-new`

- Fetch changes from the default Git remote:

`jj git fetch`
