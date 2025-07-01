# stress-ng

> Load and stress a Linux system in various ways (CPU, memory, I/O, etc.).
> Useful for benchmarking, hardware validation, and stability testing.
> More information: <https://manned.org/stress-ng>.

- Stress all CPUs with 4 workers for 60 seconds:

`stress-ng {{[-c|--cpu]}} 4 {{[-t|--timeout]}} 60s`

- Stress virtual memory with 2 workers for 30 seconds:

`stress-ng {{[-m|--vm]}} 2 --vm-bytes {{512M}} {{[-t|--timeout]}} 30s`

- Stress the I/O subsystem with 3 workers for 45 seconds:

`stress-ng {{[-i|--io]}} 3 {{[-t|--timeout]}} 45s`

- Run all stress tests for 2 minutes:

`stress-ng {{[-a|--all]}} {{1}} {{[-t|--timeout]}} 2m`
