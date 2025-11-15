# cargo generate-lockfile

> Generate the `Cargo.lock` file for the current package. Similar to `cargo update`, but has less options.
> If the lockfile already exists it will be rebuilt with latest version of every package.
> More information: <https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- Generate a `Cargo.lock` file with the latest version of every package:

`cargo generate-lockfile`
