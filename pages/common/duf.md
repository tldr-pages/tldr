# duf

> Disk Usage/Free Utility - a better 'df' alternative.
> More information: <https://github.com/muesli/duf>.

- List accessible devices:

`duf`

- List everything (including pseudo, duplicate, inaccessible file systems):

`duf --all`

- Only list specific devices or mount points:

`duf {{/path/to/directory1 /path/to/directory2}}`

- Sort the output:

`duf --sort size`
