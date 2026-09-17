# amdgpu_top

> Tool to display AMD GPU utilization and hardware metrics using the AMDGPU driver.
> See also: `nvtop`, `radeontop`.
> More information: <https://github.com/Umio-Yasuno/amdgpu_top#usage>.

- Display a list of AMDGPU devices:

`amdgpu_top --list`

- Dump all GPU processes and per-process memory usage:

`amdgpu_top {{[-p|--process]}}`

- Select a specific GPU by PCI bus:

`amdgpu_top --pci "{{0000:01:00.0}}"`

- Launch the interactive TUI monitor:

`amdgpu_top`

- Launch the GUI monitor:

`amdgpu_top --gui`

- Launch a simple SMI-like TUI view:

`amdgpu_top --smi`
