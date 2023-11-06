# rustdoc

> Generate documentation for a Rust crate.
> More information: <https://doc.rust-lang.org/stable/rustdoc>.

- Generate documentation from the crate's root:

`rustdoc {{src/lib.rs}}`

- Pass a name for the project:

`rustdoc {{src/lib.rs}} --crate-name {{name}}`

- Generate documentation from Markdown files:

`rustdoc {{path/to/file.md}}`

- Specify the output directory:

`rustdoc {{src/lib.rs}} --out-dir {{path/to/output_directory}}`
