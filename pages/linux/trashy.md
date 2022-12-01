# trashy

> An alternative to `rm` and `trash-cli` written in Rust.
> More information: <https://github.com/oberblastmeister/trashy>.

- Move a specific file to the trash:

`trash {{path/to/file}}`

- Move specific files to the trash:

`trash {{path/to/file1 path/to/file2 ...}}`

- List items in the trash:

`trash list`

- Restore a specific file from the trash:

`trash restore {{path/to/file}}`

- Remove a specific file from the trash:

`trash empty {{path/to/file}}`

- Restore all files from the trash:

`trash restore --all`

- Remove all files from the trash:

`trash empty --all`
