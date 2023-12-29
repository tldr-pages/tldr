# bpftrace

> Linguagem de análise de alto nível para eBPF Linux.
> Mais informações: <https://github.com/iovisor/bpftrace>.

- Exibe a versão do bpftrace:

`bpftrace -V`

- Lista todos os probes:

`sudo bpftrace -l`

- Roda um programa de uma linha (e.g. número de syscalls por programa):

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }}}'`

- Roda um programa de um arquivo:

`sudo bpftrace {{caminho/do/arquivo}}`

- Analisa um programa por PID:

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }}}'`

- Mostra o resultado do programa em eBPF, sem rodar ele:

`sudo bpftrace -d -e '{{programa_de_uma_linha}}'`
