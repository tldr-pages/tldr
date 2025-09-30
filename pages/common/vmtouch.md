# vmtouch

> Manage the filesystem cache.
> More information: <https://manned.org/vmtouch>.

- Print the cache status of a file:

`vmtouch {{path/to/file}}`

- Load a file into cache:

`vmtouch -t {{path/to/file}}`

- Evict a file from cache:

`vmtouch -e {{path/to/file}}`

- Lock a file in cache to prevent eviction from memory:

`vmtouch -l {{path/to/file}}`

- Lock a file and daemonize the program:

`vmtouch -ld {{path/to/file}}`
