# radeontop

> Show utilisation of AMD GPUs.
> More information: <https://github.com/clbr/radeontop>.

- Show the utilisation of the default AMD GPU (may require root privileges depending on your system):

`radeontop`

- Enable colored output:

`radeontop --color`

- Select a specific GPU (the bus number is the first number in the output of `lspci`):

`radeontop --bus {{bus_number}}`

- Specify the display refresh rate (higher means more GPU overhead):

`radeontop --ticks {{samples_per_second}}`
