# bpftrace

> Magas szintű nyomkövetési nyelv Linux eBPF számára. További információ: <https://github.com/iovisor/bpftrace>.

- A bpftrace verziójának megjelenítése:

`bpftrace -V`

- Az összes rendelkezésre álló szonda listázása:

`sudo bpftrace -l`

- Egysoros program futtatása (pl. syscall count by program):

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }}}'`

- Program futtatása egy fájlból:

`sudo bpftrace {{path/to/file}}`

- Egy program nyomon követése PID alapján:

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }}}'`

- Száraz futtatás és a kimenet megjelenítése eBPF formátumban:

`sudo bpftrace -d -e '{{one_line_program}}'`
