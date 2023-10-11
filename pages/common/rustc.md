# rustc

> The Rust compiler.
> Rust projects usually use `cargo` instead of invoking `rustc` directly.
> More information: <https://doc.rust-lang.org/rustc>.

- Compile a binary crate:

`rustc {{path/to/main.rs}}`

- Compile with optimizations (`s` means optimize for binary size; `z` is the same with even more optimizations):

`rustc -C lto -C opt-level={{0|1|2|3|s|z}} {{path/to/main.rs}}`

- Compile with debugging information:

`rustc -g {{path/to/main.rs}}`

- Explain an error message:

`rustc --explain {{error_code}}`

- Compile with architecture-specific optimizations for the current CPU:

`rustc -C target-cpu={{native}} {{path/to/main.rs}}`

- Display the target list (Note: you have to add a target using `rustup` first to be able to compile for it):

`rustc --print target-list`

- Compile for a specific target:

`rustc --target {{target_triple}} {{path/to/main.rs}}`
