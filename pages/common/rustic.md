# rustic

> Create fast, encrypted, deduplicated backups powered by Rust.
> More information: <https://github.com/rustic-rs/rustic>.

- Initialize a new repository:

`rustic init --repository {{/srv/rustic-repo}}`

- Create a new backup of a file/directory to a repository:

`rustic backup --repository {{/srv/rustic-repo}} {{path/to/file_or_directory}}`
