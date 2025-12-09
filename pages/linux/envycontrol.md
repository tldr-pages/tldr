# envycontrol

> GPU switching utility for Nvidia Optimus laptops.
> More information: <https://github.com/bayasdev/envycontrol#%EF%B8%8F-usage>.

- Switch between different GPU modes:

`sudo envycontrol {{[-s|--switch]}} {{nvidia|integrated|hybrid}}`

- Specify your [d]isplay [m]anager manually:

`envycontrol --dm {{gdm|gdm3|sddm|lightdm}}`

- Check current GPU mode:

`sudo envycontrol {{[-q|--query]}}`

- Reset settings:

`sudo envycontrol --reset`

- Display help:

`envycontrol {{[-h|--help]}}`

- Display version:

`envycontrol {{[-v|--version]}}`
