# age-inspect

> Inspect `age` encrypted files.
> See also: `age`, `age-keygen`.
> More information: <https://manned.org/age-inspect>.

- Print the recipient type, the file size, and whether it uses post-quantum encryption:

`age-inspect {{path/to/file}}`

- Inspect an age encrypted file and print the json output to `stdout`:

`age-inspect --json {{path/to/file}}`
