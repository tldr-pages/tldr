# radeontop

> Show utilization of AMD GPUs.
> May require root privileges depending on your system.
> More information: <https://github.com/clbr/radeontop/blob/master/radeontop.asc>.

- Show the utilization of the default AMD GPU:

`radeontop`

- Enable colored output:

`radeontop {{[-c|--color]}}`

- Select a specific GPU (the bus number is the first number in the output of `lspci`):

`radeontop {{[-b|--bus]}} {{bus_number}}`

- Specify the display refresh rate (higher means more GPU overhead):

`radeontop {{[-t|--ticks]}} {{samples_per_second}}`
