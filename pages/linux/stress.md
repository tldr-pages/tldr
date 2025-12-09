# stress

> Stress test CPU, memory, and IO on a Linux system.
> More information: <https://manned.org/stress>.

- Spawn 4 workers to stress test CPU:

`stress {{[-c|--cpu]}} {{4}}`

- Spawn 2 workers to stress test IO and timeout after 5 seconds:

`stress {{[-i|--io]}} {{2}} {{[-t|--timeout]}} {{5}}`

- Spawn 2 workers to stress test memory (each worker allocates 256M bytes):

`stress {{[-m|--vm]}} {{2}} --vm-bytes {{256M}}`

- Spawn 2 workers spinning on write()/unlink() (each worker writes 1G bytes):

`stress {{[-d|--hdd]}} {{2}} --hdd-bytes {{1GB}}`
