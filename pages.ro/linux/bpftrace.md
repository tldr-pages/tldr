# bpftrace

> Limba de urmărire la nivel înalt pentru Linux EBPF.
> Mai multe informaţii: <https://github.com/iovisor/bpftrace>

- Afișează versiunea bpftrace:

`bpftrace -V`

- Listează toate sondele disponibile:

`sudo bpftrace -l`

- Rulați un program cu o singură linie (de exemplu, numărul syscall după program):

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }}}'`

- Rulați un program dintr-un fișier:

`sudo bpftrace {{path/to/file}}`

- Urmăriți un program de PID:

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }}}'`

- Faceți o rulare uscată și afișați ieșirea în format EBPF:

`sudo bpftrace -d -e '{{one_line_program}}'`
