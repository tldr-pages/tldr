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

- Show or hide specific filesystems:

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- Sort the output by key:

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- Change the theme (if `duf` fails to use the right theme):

`duf --theme {{dark|light}}`
