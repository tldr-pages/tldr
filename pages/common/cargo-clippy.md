# cargo clippy

> A collection of lints to catch common mistakes and improve your Rust code.
> More information: <https://github.com/rust-lang/rust-clippy>.

- Run checks over the code in the current directory:

`cargo clippy`

- Require that `Cargo.lock` is up to date:

`cargo clippy --locked`

- Run checks on all packages in the workspace:

`cargo clippy --workspace`

- Run checks for a package:

`cargo clippy --package {{package}}`

- Run checks for a lint group (see <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious>):

`cargo clippy -- {{[-W|--warn]}} clippy::{{lint_group}}`

- Treat warnings as errors:

`cargo clippy -- {{[-D|--deny]}} warnings`

- Run checks and ignore warnings:

`cargo clippy -- {{[-A|--allow]}} warnings`

- Apply Clippy suggestions automatically:

`cargo clippy --fix`
