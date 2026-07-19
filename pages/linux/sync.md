# sync

> Flush pending write operations to disk.
> See also: `sync` for common usage.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- Flush all pending write operations on all disks:

`sync`

- Flush all pending write operations on a single file to disk:

`sync {{path/to/file}}`

- Flush writes and drop filesystem caches:

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`
