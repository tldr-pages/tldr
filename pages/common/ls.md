# ls

> List directory contents.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- List files one per line:

`ls -1`

- List all files, including hidden files:

`ls {{[-a|--all]}}`

- List files with a trailing symbol to indicate file type (directory/, symbolic_link@, executable*, ...):

`ls {{[-F|--classify]}}`

- List all files in [l]ong format (permissions, ownership, size, and modification date):

`ls {{[-la|-l --all]}}`

- List files in [l]ong format with size displayed using human-readable units (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- List files in [l]ong format, sorted by [S]ize (descending) recursively:

`ls {{[-lSR|-lS --recursive]}}`

- List files in [l]ong format, sorted by [t]ime the file was modified and in reverse order (oldest first):

`ls {{[-ltr|-lt --reverse]}}`

- Only list directories:

`ls {{[-d|--directory]}} */`
