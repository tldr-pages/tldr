# cargo search

> Search for packages on <https://crates.io>.
> The crates are displayed along with descriptions in TOML format suitable for copying into `Cargo.toml`.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-search.html>.

- Search for packages:

`cargo search {{query}}`

- Show `n` results (default: 10, max: 100):

`cargo search --limit {{n}} {{query}}`
