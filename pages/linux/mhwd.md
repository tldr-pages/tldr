# mhwd

> Manjaro Hardware Detection utility  .
> More information: <https://wiki.manjaro.org/index.php/Manjaro_Hardware_Detection_Overview>.

- [l]ist available drivers:

`mhwd {{[-l|--list]}}`

- [l]ist [i]nstalled drivers:

`mhwd {{[-li|--listinstalled]}}`

- [i]nstall a driver:

`mhwd {{[-i|--install]}} {{pci|usb}} {{driver_name}}`

- [r]emove a driver:

`mhwd {{[-r|--remove]}} {{pci|usb}} {{driver_name}}`

- Display [d]etailed information about detected hardware:

`mhwd {{[-l|--list]}} {{[-d|--detail]}}`

- [a]utomatically install best available driver for the detected graphics card:

`mhwd {{[-a|--auto]}} pci {{free|nonfree}} 0300`
