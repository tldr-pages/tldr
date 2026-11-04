# enable

> Enable and disable shell builtins.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-enable>.

- Print the list of builtins:

`enable`

- Disable a builtin (works in Bash only):

`enable -n {{command}}`

- Re-enable a builtin:

`enable {{command}}`

- Load a new builtin from a shared object:

`enable -f {{path/to/file.so}} {{builtin_name}}`

- Display help:

`help enable`
