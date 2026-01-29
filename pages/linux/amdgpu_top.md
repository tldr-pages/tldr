# amdgpu_top

> Display AMD GPU utilization and hardware metrics in TUI, GUI, or JSON modes.
> See also: `nvtop`, `radeontop`.
> More information: <https://github.com/Umio-Yasuno/amdgpu_top>.

- Launch the interactive TUI monitor:

`amdgpu_top`

- Launch the GUI monitor:

`amdgpu_top --gui`

- Show a simple SMI-like text view:

`amdgpu_top --smi`

- Dump detailed AMDGPU information (specs, VRAM, PCI, VBIOS, etc.):

`amdgpu_top --dump`

- Dump AMDGPU information and gpu_metrics in JSON format:

`amdgpu_top --dump --gpu-metrics --json`
