# sync

> Flushes all pending write operations to the appropriate disks.
> More information: <https://keith.github.io/xcode-man-pages/sync.8.html>.

- Flush all pending write operations on all disks:

`sync`

- Flush all pending write operations on a single file to disk:

`sync {{path/to/file}}`

- Flush disk writes and attempts to clear inactive memory and filesystem caches:

`sync; sudo purge`
