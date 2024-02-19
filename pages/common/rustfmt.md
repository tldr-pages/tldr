# rustfmt

> Format Rust source code.
> More information: <https://github.com/rust-lang/rustfmt>.

- Format a file, overwriting the original file in-place:

`rustfmt {{path/to/source.rs}}`

- Check a file for formatting and display any changes on the console:

`rustfmt --check {{path/to/source.rs}}`

- Backup any modified files before formatting (the original file is renamed with a `.bk` extension):

`rustfmt --backup {{path/to/source.rs}}`
