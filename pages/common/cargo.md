# cargo

> Rust package manager.
> Manage Rust projects and their module dependencies (crates).

- Search for crates:

`cargo search {{search_string}}`

- Install a crate:

`cargo install {{crate_name}}`

- List installed crates:

`cargo install --list`

- Create a new binary Rust project in the current directory:

`cargo init --bin`

- Create a new library Rust project in the current directory:

`cargo init`

- Build the Rust project in the current directory:

`cargo build`

- Build with multiple parallel jobs:

`cargo build -j {{jobs}}`
