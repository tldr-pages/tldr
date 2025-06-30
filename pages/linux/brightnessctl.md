# brightnessctl

> Utility for reading and controlling device brightness for Linux operating systems.
> More information: <https://github.com/Hummer12007/brightnessctl#usage>.

- List devices with changeable brightness:

`brightnessctl {{[-l|--list]}}`

- Print the current brightness of the display backlight:

`brightnessctl get`

- Set the brightness of the display backlight to a specified percentage within range:

`brightnessctl set {{50%}}`

- Increase brightness by a specified increment:

`brightnessctl set {{+10%}}`

- Decrease brightness by a specified decrement:

`brightnessctl set {{10%-}}`
