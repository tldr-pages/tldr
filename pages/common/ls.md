# ls

> List directory contents.
> More information: <https://www.gnu.org/software/coreutils/ls>.

- List files one per line:

`ls -1`

- List [a]ll files, including hidden files:

`ls -a`

- List files with a trailing symbol to indicate file type (directory/, symbolic_link@, executable*, ...):

`ls -F`

- List [a]ll files in [l]ong format (permissions, ownership, size, and modification date):

`ls -la`

- [l]ong format list with size displayed using [h]uman-readable units (KiB, MiB, GiB):

`ls -lh`

- [l]ong format list sorted by [S]ize (descending) [R]ecursively:

`ls -lSR`

- [l]ong format list of files, sorted by [t]ime it was modified and in [r]everse order (oldest first):

`ls -ltr`

- Only list [d]irectories:

`ls -d */`
