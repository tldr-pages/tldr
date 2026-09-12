# mado

> A fast Markdown linter for CommonMark and GitHub Flavored Markdown.
> More information: <https://github.com/akiomik/mado>.

- Check all Markdown files in the current directory recursively:

`mado check`

- Check specific files or directories:

`mado check {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Exclude files matching a `glob` pattern:

`mado check --exclude "{{**/node_modules/**}}" {{path/to/directory}}`

- Check using a specific configuration file:

`mado --config {{path/to/mado.toml}} check {{path/to/directory}}`

- Display violations in a specific format:

`mado check {{path/to/directory}} --output-format {{concise|mdl|markdownlint}}`

- Generate a completion script for a specific shell:

`mado generate-shell-completion {{bash|elvish|fish|powershell|zsh}}`

- Display help:

`mado --help`

- Display version:

`mado --version`
