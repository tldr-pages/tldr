# cargo yank

> Remove a pushed crate from the index. This should only be used when you accidentally release a significantly broken crate.
> Note: this does not remove any data. The crate is still present after a yank - this just prevents new projects from using it.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- Yank the specified version of a crate:

`cargo yank {{crate}}@{{version}}`

- Undo a yank (i.e. allow downloading it again):

`cargo yank --undo {{crate}}@{{version}}`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo yank --registry {{name}} {{crate}}@{{version}}`
