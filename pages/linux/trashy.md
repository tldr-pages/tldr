# trashy

> An alternative to `rm` and `trash-cli` written in Rust.
> More information: <https://github.com/oberblastmeister/trashy>.

- Trash several files:

`trash {{path/to/file}}`

- Move specific files to the trash:

`trash {{path/to/file1 path/to/file2 ...}}`

- List items in the trash:

`trash list`

- Restore file from trash:

`trash restore {{file}}`

- Empty file from trash:

`trash empty {{file}}`

- Restore all files:

`trash restore --all`

- Empty all files:

`trash empty --all`
