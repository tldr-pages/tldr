# cargo package

> Assemble a local package into a distributable tarball (a `.crate` file).
> Similar to `cargo publish --dry-run`, but has more options.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-package.html>.

- Perform checks and create a `.crate` file (equivalent of `cargo publish --dry-run`):

`cargo package`

- Display what files would be included in the tarball without actually creating it:

`cargo package --list`
