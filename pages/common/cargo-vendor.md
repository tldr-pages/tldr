# cargo vendor

> Vendor all dependencies of a project into the specified directory (default: `vendor`).
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>.

- Vendor dependencies and configure `cargo` to use the vendored sources in the current project:

`cargo vendor {{path/to/directory}} > .cargo/config.toml`
