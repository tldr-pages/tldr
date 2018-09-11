# rustfmt

> Tool for formatting Rust source code.

- Format a file, overwriting the original file in-place:

`rustfmt {{source.rs}}`

- Check a file for formatting and display any changes on console:

`rustfmt --check {{source.rs}}`

- Backup any modified files before formatting (if a file `source.rs` is formated, the backup is `source.bk`):

`rustfmt --backup {{source.rs}}`
