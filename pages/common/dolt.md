# dolt

> Dolt is an SQL database that you can fork, clone, branch, merge, push and pull just like a Git repository.
> Some subcommands such as `dolt commit` have their own usage documentation.
> More information: <https://github.com/dolthub/dolt>.

- Execute a dolt subcommand:

`dolt {{subcommand}}`

- List available subcommands:

`dolt init`  - Create an empty Dolt data repository.

`dolt status`  - Show the working tree status.

`dolt add`  - Add table changes to the list of staged table changes.

`dolt diff`  - Diff a table.

`dolt reset`  - Remove table changes from the list of staged table vchanges.

`dolt clean`  - Remove untracked tables from working set.

`dolt commit`  - Record changes to the repository.

`dolt sql`  - Run a SQL query against tables in repository.

`dolt sql-server`  - Start a MySQL-compatible server.

`dolt sql-client`  - Starts a built-in MySQL client.

`dolt log`  - Show commit logs.

`dolt branch`  - Create, list, edit, delete branches.

`dolt checkout`  - Checkout a branch or overwrite a table from HEAD.

`dolt merge`  - Merge a branch.

`dolt conflicts`  - Commands for viewing and resolving merge conflicts.

`dolt cherry-pick`  - Apply the changes introduced by an existing commit.

`dolt revert`  - Undo the changes introduced in a commit.

`dolt clone`  - Clone from a remote data repository.

`dolt fetch`  - Update the database from a remote data repository.

`dolt pull`  - Fetch from a dolt remote data repository and merge.

`dolt push`  - Push to a dolt remote.

`dolt config`  - Dolt configuration.

`dolt remote`  - Manage set of tracked repositories.

`dolt backup`  - Manage a set of server backups.

`dolt login`  - Login to a dolt remote host.

`dolt creds`  - Commands for managing credentials.

`dolt ls`  - List tables in the working set.

`dolt schema`  - Commands for showing and importing table schemas.

`dolt table`  - Commands for copying, renaming, deleting, and exporting tables.

`dolt tag`  - Create, list, delete tags.

`dolt blame`  - Show what revision and author last modified each row of a table.

`dolt constraints`  - Commands for handling constraints.

`dolt migrate`  - Executes a database migration to use the latest Dolt data format.

`dolt read-tables`  - Fetch table(s) at a specific commit into a new dolt repo

`dolt gc`  - Cleans up unreferenced data from the repository.

`dolt filter-branch`  - Edits the commit history using the provided query.

`dolt merge-base`  - Find the common ancestor of two commits.

`dolt version`  - Displays the current Dolt cli version.

`dolt dump`  - Export all tables in the working set into a file.
