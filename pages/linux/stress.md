# stress

> Stress test CPU, memory, and IO on a Linux system.
> More information: <https://manned.org/stress>.

- Spawn 4 workers to stress test CPU:

`stress -c {{4}}`

- Spawn 2 workers to stress test IO and timeout after 5 seconds:

`stress -i {{2}} -t {{5}}`

- Spawn 2 workers to stress test memory (each worker allocates 256M bytes):

`stress -m {{2}} --vm-bytes {{256M}}`

- Spawn 2 workers spinning on write()/unlink() (each worker writes 1G bytes):

`stress -d {{2}} --hdd-bytes {{1GB}}`
