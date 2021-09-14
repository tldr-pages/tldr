# brightnessctl

> Utility for reading and controlling device brightness for GNU/Linux operating systems.
> More information: <https://github.com/Hummer12007/brightnessctl>.

- List devices with available brightness control:

`brightnessctl --list`

- Get the currently set brightness of the display backlight:

`brightnessctl get`

- Set the brightness of the display backlight to a percenage of the maximum supported value:

`brightnessctl set {{50%}}`

- Increase brightness by certain percent (eg. 10%):

`brightnessctl set {{+10%}}`

- Decrease brightness by certain percent (eg. 10%):

`brightnessctl set {{-10%}}`
