# sync

> Force completion of pending disk writes.
> See also: `purge`.
> More information: <https://keith.github.io/xcode-man-pages/sync.8.html>.

- Flush all pending disk writes:

`sync`

- Flush disk writes, then clear inactive memory and filesystem caches:

`sync; sudo purge`
