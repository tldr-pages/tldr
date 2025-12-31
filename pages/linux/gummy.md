# gummy

> Screen brightness/temperature manager for Linux/X11.
> More information: <https://github.com/Gitoffthelawn/gummy>.

- Set the screen temperature to 3000K:

`gummy {{[-t|--temperature]}} {{3000}}`

- Set the screen backlight to 50%:

`gummy --backlight {{50}}`

- Set the screen pixel brightness to 45%:

`gummy {{[-b|--brightness]}} {{45}}`

- Increase current screen pixel brightness by 10%:

`gummy {{[-b|--brightness]}} {{+10}}`

- Decrease current screen pixel brightness by 10%:

`gummy {{[-b|--brightness]}} {{-10}}`

- Set the temperature and pixel brightness for the second screen:

`gummy {{[-s|--screen]}} {{1}} {{[-t|--temperature]}} {{3800}} {{[-b|--brightness]}} {{65}}`
