# rustic

> Create fast, encrypted, deduplicated backups powered by Rust.
> More information: <https://github.com/rustic-rs/rustic>.

- Initialize a new repository in `~/backup`:

`rustic init --repository ~/backup`

- Create a new backup of `~/important_stuff` to the repository `~/backup`:

`rustic backup --repository ~/backup ~/important_stuff`
