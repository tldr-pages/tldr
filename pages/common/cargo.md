# cargo

> Rust package manager.
> Manage Rust projects and their module dependencies (crates).
> More information: <https://crates.io/>.

- Search for crates:

`cargo search {{search_string}}`

- Install a crate:

`cargo install {{crate_name}}`

- List installed crates:

`cargo install --list`

- Create a new binary or library Rust project in the current directory:

`cargo init --{{bin|lib}}`

- Create a new binary or library Rust project in the specified directory:

`cargo new {{path/to/directory}} --{{bin|lib}}`

- Build the Rust project in the current directory:

`cargo build`

- Build using a specific number of threads (default is the number of CPU cores):

`cargo build -j {{jobs}}`
