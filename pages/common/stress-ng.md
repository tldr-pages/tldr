# stress-ng

> A tool to load and stress a Linux system in various ways (CPU, memory, I/O, etc.).
Useful for benchmarking, hardware validation, and stability testing.
> More information: https://manpages.ubuntu.com/manpages/focal/man1/stress-ng.1.html.

- Stress all CPUs with 4 workers for 60 seconds:

`stress-ng --cpu {{4}} --timeout {{60s}}`

- Stress virtual memory with 2 workers for 30 seconds:

`stress-ng --vm {{2}} --vm-bytes {{512M}} --timeout {{30s}}`

- Stress the I/O subsystem with 3 workers:

`stress-ng --io {{3}} --timeout {{45s}}`

- Run all stress tests for 2 minutes:

`stress-ng --all {{1}} --timeout {{2m}}`
