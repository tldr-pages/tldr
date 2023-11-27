# cargo clean

> Remove generated artifacts in the `target` directory.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- Remove the entire `target` directory:

`cargo clean`

- Remove documentation artifacts (the `target/doc` directory):

`cargo clean --doc`

- Remove release artifacts (the `target/release` directory):

`cargo clean --release`

- Remove artifacts in the directory of the given profile (in this case, `target/debug`):

`cargo clean --profile {{dev}}`
