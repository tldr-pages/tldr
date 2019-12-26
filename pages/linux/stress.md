# stress

> A tool to stress test CPU, memory, and IO on a Linux system.

- Spawn N workers to stress test CPU:

`stress -c {{N}}`

- Spawn N workers to stress test IO and timeout after M seconds:

`stress -i {{N}} -t {{M}}`

- Spawn N workers to stress test memory(each worker malloc 256M bytes):

`stress -m {{N}} --vm-bytes 256M`

- Spawn N workds spinning on write()/unlink()(each worker write 1G bytes):

`stress -d {{N}} --hdd-bytes 1GB`
