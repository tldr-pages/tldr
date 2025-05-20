# vol.py

> Forensics framework used to analyze volatile memory (RAM) dumps.
> With volatility3, plugins are now based on operating system. Examples below will use Windows.
> More information: <https://volatility3.readthedocs.io/en/latest/index.html>.

- Get information about a memory dump file:

`python3 vol.py {{[-f|--filename]}} {{path/to/memory_dump_file}} windows.info`

- List active processes:

`python3 vol.py {{[-f|--filename]}} {{path/to/memory_dump_file}} windows.pslist`

- List hashes of users on system:

`python3 vol.py {{[-f|--filename]}} {{path/to/memory_dump_file}} windows.hashdump`

- List active network connections:

`python3 vol.py {{[-f|--filename]}} {{path/to/memory_dump_file}} windows.netstat`

- Display help:

`python3 vol.py {{[-h|--help]}}`
