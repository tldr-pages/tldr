# cargo install

> Build and install a Rust binary.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-install.html>.

- Install a package from <https://crates.io> (the version is optional - latest by default):

`cargo install {{package}}@{{version}}`

- Install a package from the specified Git repository:

`cargo install --git {{repo_url}}`

- Build from the specified branch/tag/commit when installing from a Git repository:

`cargo install --git {{repo_url}} --{{branch|tag|rev}} {{branch_name|tag|commit_hash}}`

- List all installed packages and their versions:

`cargo install --list`
