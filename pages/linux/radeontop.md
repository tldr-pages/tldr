# radeontop

> Show utilization of AMD GPUs.
> May require root privileges depending on your system.
> More information: <https://github.com/clbr/radeontop>.

- Show the utilization of the default AMD GPU:

`radeontop`

- Enable colored output:

`radeontop --color`

- Select a specific GPU (the bus number is the first number in the output of `lspci`):

`radeontop --bus {{bus_number}}`

- Specify the display refresh rate (higher means more GPU overhead):

`radeontop --ticks {{samples_per_second}}`
