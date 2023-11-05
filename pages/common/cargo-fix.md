# cargo fix

> Automatically fix lint warnings reported by `rustc`.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- Fix code even if it already has compiler errors:

`cargo fix --broken-code`

- Fix code even if the working directory has changes:

`cargo fix --allow-dirty`

- Migrate a package to the next Rust edition:

`cargo fix --edition`

- Fix the package’s library:

`cargo fix --lib`

- Fix the specified integration test:

`cargo fix --test {{name}}`

- Fix all members in the workspace:

`cargo fix --workspace`
