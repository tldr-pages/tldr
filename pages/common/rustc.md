# rustc

> The Rust compiler.
> Processes, compiles and links Rust language source files.
> More information: <https://doc.rust-lang.org/rustc>.

- Compile a single file:

`rustc {{path/to/file.rs}}`

- Compile with high optimization:

`rustc -O {{path/to/file.rs}}`

- Compile with debugging information:

`rustc -g {{path/to/file.rs}}`

- Compile with architecture-specific optimizations for the current CPU:

`rustc -C target-cpu=native {{path/to/file.rs}}`

- Display architecture-specific optimizations for the current CPU:

`rustc -C target-cpu=native --print cfg`

- Display target list:

`rustc --print target-list`

- Compile for a specific target:

`rustc --target {{target_triple}} {{path/to/file.rs}}`
