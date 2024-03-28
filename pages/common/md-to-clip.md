# md-to-clip

> Convert tldr-pages to Command Line Interface Pages.
> See also: `clip-view`.
> More information: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>.

- Convert tldr-pages files and save into the same directories:

`md-to-clip {{path/to/page1.md path/to/page2.md ...}}`

- Convert tldr-pages files and save into a specific directory:

`md-to-clip --output-directory {{path/to/directory}} {{path/to/page1.md path/to/page2.md ...}}`

- Convert a tldr-page file to `stdout`:

`md-to-clip --no-file-save <(echo '{{page-content}}')`

- Convert tldr-pages files while recognizing additional placeholders from a specific config:

`md-to-clip --special-placeholder-config {{path/to/config.yaml}} {{path/to/page1.md path/to/page2.md ...}}`

- Display help:

`md-to-clip --help`

- Display version:

`md-to-clip --version`
