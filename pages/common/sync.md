# sync

> Flushes all pending write operations to the appropriate disks.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- Flush all pending write operations on all disks:

`sync`

- Flush all pending write operations on a single file to disk:

`sync {{path/to/file}}`

- Flush writes and drop file system caches (Linux only):

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`

- Flush disk writes and attempts to clear inactive memory and filesystem caches (macOS only):

`sync; sudo purge`
