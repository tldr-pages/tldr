# cargo deb

> Create Debian packages from Cargo projects.
> More information: <https://github.com/kornelski/cargo-deb>.

- Create a Debian package from a project:

`cargo deb`

- Write the `.deb` file to the specified file or directory:

`cargo deb {{[-o|--output]}} {{path/to/file_or_directory}}`

- Compile for the specified Rust target triple:

`cargo deb --target {{x86_64-unknown-linux-gnu}}`

- Select which package to use in a Cargo workspace:

`cargo deb {{[-p|--package]}} {{package_name}}`

- Immediately install the created package:

`cargo deb --install`
