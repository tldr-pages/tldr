# melt

> Generate seed phrases from SSH keys for backup and recovery.
> More information: <https://github.com/charmbracelet/melt>.

- Generate a seed phrase from an SSH key:

`melt {{path/to/ssh_key}}`

- Generate a seed phrase and save to file:

`melt {{path/to/ssh_key}} > {{seed_file}}`

- Restore an SSH key from a seed phrase:

`melt restore --seed "{{seed_phrase}}" {{path/to/output_key}}`

- Restore an SSH key from a seed file:

`melt restore {{path/to/output_key}} < {{seed_file}}`

- Generate seed phrase in a specific language:

`melt --language {{language}} {{path/to/ssh_key}}`

- Display version information:

`melt --version`

- Display help:

`melt --help`
