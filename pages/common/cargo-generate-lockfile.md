# cargo generate-lockfile

> Generates the Cargo.lock file for the current package.  
> If the lockfile already exsits it will be rebuilt with latest version of every package.
> More information: <https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- Generate Cargo.lock with latest version of every package:

`cargo generate-lockfile`

- Path for the `Cargo.toml` file. By default the file is present in the current directory:

`cargo generate-lockfile --manifest-path {{path/to/toml/file}}`

- Assert that the `Cargo.lock` file is up-to-date:

`cargo generate-lockfile --locked`

- Prevent the Cargo from attempting to access the network to determine if it out-of-date:

`cargo generate-lockfile --frozen`

- Prevent Cargo from accessing the network. Cargo will attempt to proceed without network. If Cargo requires internet to proceed and network is not available Cargo will stop with an error:
 
`cargo generate-lockfile --offline`
