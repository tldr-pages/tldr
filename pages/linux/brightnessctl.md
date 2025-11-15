# brightnessctl

> Utility for reading and controlling device brightness for Linux operating systems.
> More information: <https://github.com/Hummer12007/brightnessctl#usage>.

- List devices with changeable brightness:

`brightnessctl {{[-l|--list]}}`

- Print the current brightness of the default device:

`brightnessctl {{[g|get]}}`

- Print the current brightness of a specific device (can be a wildcard):

`brightnessctl {{[g|get]}} {{[-d|--device]}} '{{device_name}}'`

- Set the brightness to a specified percentage:

`brightnessctl {{[s|set]}} {{50}}%`

- Increase brightness by a specified percentage:

`brightnessctl {{[s|set]}} +{{10}}%`

- Decrease brightness by a specified percentage:

`brightnessctl {{[s|set]}} {{10}}%-`
