# cargo init

> Create a new Cargo package.
> Equivalent of `cargo new`, but specifiying a directory is optional.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- Initialize a Rust project with a binary target in the current directory:

`cargo init`

- Initialize a Rust project with a binary target in the specified directory:

`cargo init {{path/to/directory}}`

- Initialize a Rust project with a library target in the current directory:

`cargo init --lib`

- Initialize a version control system repository in the project directory (default: `git`):

`cargo init --vcs {{git|hg|pijul|fossil|none}}`

- Set the package name (default: directory name):

`cargo init --name {{name}}`
