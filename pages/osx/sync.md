# sync

> Flush pending write operations to disk.
> See also: `sync` for common usage, `purge`.
> More information: <https://keith.github.io/xcode-man-pages/sync.8.html>.

- Flush all pending write operations on all disks:

`sync`

- Flush disk writes, then clear inactive memory and filesystem caches:

`sync; sudo purge`
