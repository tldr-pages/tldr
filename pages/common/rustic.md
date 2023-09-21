# rustic

> Create fast, encrypted, deduplicated backups powered by Rust
> More Information: https://github.com/rustic-rs/rustic

- Initialize a new repository in `~/backup`

`rustic init -r ~/backup`

- Create a new backup of `~/important_stuff` to the repository `~/backup`

`rustic backup -r ~/backup ~/important_stuff`
