# envycontrol

> GPU switching utility for Nvidia Optimus laptops.
> More information: <https://github.com/bayasdev/envycontrol>.

- Display help: 
`envycontrol --help`

- Display version:

`envycontrol --version`

- Specify your display manager manually:

`envycontrol --dm`

- Reset settings:


`sudo envycontrol --reset`

> Switch Graphic Mode:

- Check Current Graphic Mode

`sudo envycontrol --query`

- Switch to NVIDIA Graphic:

`sudo envycontrol -s nvidia`

- Switch to Integrated Graphic

`sudo envycontrol -s integrated`

- Switch to hybrid Graphic

`sudo envycontrol -s {{nvidia|integrated|hybrid}}`
