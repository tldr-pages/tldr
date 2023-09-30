# cargo fix

> Automatically fix lint warnings reported by rustc.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- Fix code even if it already has compiler errors:

`cargo fix --broken-code`

- Fix code even if the working directory has changes:

`cargo fix --allow-dirty`

- Fix the package’s library:

`cargo fix --lib`

- Fix the specified integration test:

`cargo fix --test`

- Fix all members in the workspace:

`cargo fix --workspace`

- Directory for all generated artifacts and intermediate files:

`cargo fix --target-dir`

- Prevents Cargo from accessing the network for any reason:

`cargo fix --offline`

- Number of parallel jobs to run:

`cargo fix --jobs`
