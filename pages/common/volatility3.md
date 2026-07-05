# volatility3

> Cross-platform memory forensics framework.
> Analyze memory dumps from Windows, Linux, and macOS systems.
> More information: <https://github.com/volatilityfoundation/volatility3>.

- List available plugins for a memory image:

`volatility3 -f {{path/to/memory_dump}} windows.info`

- Identify the operating system of the memory image:

`volatility3 -f {{path/to/memory_dump}} windows.info`

- List running processes:

`volatility3 -f {{path/to/memory_dump}} windows.pslist`

- List processes with process tree:

`volatility3 -f {{path/to/memory_dump}} windows.pstree`

- List network connections:

`volatility3 -f {{path/to/memory_dump}} windows.netscan`

- Extract a process memory by PID:

`volatility3 -f {{path/to/memory_dump}} windows.memmap --pid {{PID}} --dump`

- List loaded kernel modules:

`volatility3 -f {{path/to/memory_dump}} windows.modules`

- Scan for command-line arguments:

`volatility3 -f {{path/to/memory_dump}} windows.cmdline`
