# cargo check

> Check a local package and all of its dependencies for errors.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- Check the current package:

`cargo check`

- Check all tests:

`cargo check --tests`

- Check the integration tests in `tests/integration_test1.rs`:

`cargo check --test {{integration_test1}}`

- Check the current package with the features `feature1` and `feature2`:

`cargo check --features {{feature1,feature2}}`

- Check the current package with default features disabled:

`cargo check --no-default-features`
