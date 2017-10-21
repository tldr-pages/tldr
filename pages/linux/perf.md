# perf

> Framework for linux performance counter measurements.

- Display basic performance counter stats for a command `gcc -c -O3 hello.c`:

`perf stat {{gcc -c -O3 hello.c}}`

- Display system-wide real time performance counter profile:

`sudo perf top`

- Run a command and record its profile into "perf.data":

`sudo perf record {{command}}`

- Read "perf.data" (created by `perf record`) and display the profile:

`sudo perf report`
