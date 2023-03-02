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

- Switch between different GPU modes:

`sudo envycontrol -s {{nvidia|integrated|hybrid}}`
