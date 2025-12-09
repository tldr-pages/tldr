# getArch.py

> Determine the OS architecture (x86 or x64) of a remote Windows system.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Check the architecture of a single target system:

`getArch.py -target {{target}}`

- Check the architecture of multiple targets from a file (one per line):

`getArch.py -targets {{path/to/targets_file}}`

- Set a custom socket timeout (default is 2 seconds):

`getArch.py -target {{target}} -timeout {{seconds}}`

- Enable debug mode for detailed output:

`getArch.py -target {{target}} -debug`
