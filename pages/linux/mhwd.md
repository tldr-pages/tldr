# mhwd

> Manjaro Hardware Detection utility.
> More information: <https://wiki.manjaro.org/index.php/Manjaro_Hardware_Detection_Overview>.

- List available drivers:

`mhwd {{[-l|--list]}}`

- List installed drivers:

`mhwd {{[-li|--listinstalled]}}`

- Install a driver:

`mhwd {{[-i|--install]}} {{pci|usb}} {{driver_name}}`

- Remove a driver:

`mhwd {{[-r|--remove]}} {{pci|usb}} {{driver_name}}`

- Display detailed information about detected hardware:

`mhwd {{[-l|--list]}} {{[-d|--detail]}}`

- Automatically install best available driver for the detected graphics card:

`mhwd {{[-a|--auto]}} pci {{free|nonfree}} 0300`
