# nvtop

> Interactive ncurses-based GPU process and status viewer for AMD, Intel, and NVIDIA GPUs.
> See also: `amdgpu_top`, `radeontop`.
> More information: <https://github.com/Syllo/nvtop>.

- Launch the interactive GPU monitor:

`nvtop`

- Set the update delay in tenths of a second (for example, 2 = 0.2 seconds):

`nvtop {{[-d|--delay]}} {{2}}`

- Run in monochrome (no color) mode:

`nvtop {{[-C|--no-color]}}`

- Use Fahrenheit for temperature display:

`nvtop {{[-f|--freedom-unit]}}`

- Always show encoder/decoder meters, disabling auto-hide:

`nvtop {{[-E|--encode-hide]}} {{-1}}`

- Show a single combined bar plot instead of per-GPU plots:

`nvtop {{[-p|--no-plot]}}`

- Show the program version:

`nvtop {{[-v|--version]}}`

