# share

> Make local resource/filesystem available for mounting by remote systems.
> More information: <https://docs.oracle.com/cd/E36784_01/html/E36825/gntjt.html>.

- List all currently shared file systems:

`share`

- Share a directory with read/write access:

`share -F nfs -o rw {{/path/to/directory}}`

- Share a directory with read-only access:

`share -F nfs -o ro {{/path/to/directory}}`

- Share a directory with specific options (e.g., allow root access from a specific host):

`share -F nfs -o rw,root={{hostname}} {{/path/to/directory}}`

- Make sharing persistent by adding entries to `/etc/dfs/dfstab`:

`echo "share -F nfs -o rw {{/path/to/directory}}" >> /etc/dfs/dfstab`
