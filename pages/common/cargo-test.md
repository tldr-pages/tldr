# cargo test

> Execute the unit and integration tests of a Rust package.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Only run tests containing a specific string in their names:

`cargo {{[t|test]}} {{test_name}}`

- Set the number of simultaneous running test cases:

`cargo {{[t|test]}} -- --test-threads {{count}}`

- Test artifacts in release mode, with optimizations:

`cargo {{[t|test]}} {{[-r|--release]}}`

- Test all packages in the workspace:

`cargo {{[t|test]}} --workspace`

- Run tests for a specific package:

`cargo {{[t|test]}} {{[-p|--package]}} {{package}}`

- Run tests without hiding output from test executions:

`cargo {{[t|test]}} -- --nocapture`
