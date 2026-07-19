# sync

> Flush pending write operations to disk (GNU coreutils).
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- Flush all pending write operations on all disks:

`sync`

- Flush pending writes for specific files:

`sync {{path/to/file1 path/to/file2 ...}}`

- Flush pending writes for specific filesystems:

`sync {{[-f|--file-system]}} {{path/to/file1 path/to/file2 ...}}`

- Flush pending writes, then drop pagecache, dentries, and inodes:

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`
