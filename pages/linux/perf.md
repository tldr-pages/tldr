# perf

> Framework for linux performance counter measurements.

- Display basic performance counter stats for a command:

`perf stat {{gcc hello.c}}`

- Display system-wide real time performance counter profile:

`sudo perf top`

- Run a command and record its profile into `perf.data`:

`sudo perf record {{command}}`

- Read `perf.data` (created by `perf record`) and display the profile:

`sudo perf report`
