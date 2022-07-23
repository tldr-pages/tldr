# duf

> Disk Usage/Free Utility.
> More information: <https://github.com/muesli/duf>.

- List accessible devices:

`duf`

- List everything (such as pseudo, duplicate or inaccessible file systems):

`duf --all`

- Only show specified devices or mount points:

`duf {{path/to/directory1 path/to/directory2 ...}}`

- Sort the output by a specified criteria:

`duf --sort {{size|used|avail|usage}}`
