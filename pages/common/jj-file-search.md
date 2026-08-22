# jj file search

> Search for content in files in a `jj` repository.
> See also: `jj file list`, `jj file show`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-search>.

- Search for files containing a `regex` in the working copy:

`jj file search {{[-p|--pattern]}} "{{regex}}"`

- Search for files containing a glob pattern:

`jj file search {{[-p|--pattern]}} "{{glob:*pattern*}}"`

- Search for content in files in a specific revision:

`jj file search {{[-r|--revision]}} {{revision}} {{[-p|--pattern]}} "{{pattern}}"`

- Search only within specific paths or files:

`jj file search {{[-p|--pattern]}} "{{pattern}}" {{path/to/file_or_directory}}`
