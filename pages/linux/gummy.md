# gummy

> Screen brightness/temperature manager for Linux/X11.
> More information: <http://web.archive.org/web/20230717200025/https://github.com/Fushko/gummy>.

- Set the screen temperature to 3000K:

`gummy --temperature {{3000}}`

- Set the screen backlight to 50%:

`gummy --backlight {{50}}`

- Set the screen pixel brightness to 45%:

`gummy --brightness {{45}}`

- Increase current screen pixel brightness by 10%:

`gummy --brightness {{+10}}`

- Decrease current screen pixel brightness by 10%:

`gummy --brightness {{-10}}`

- Set the temperature and pixel brightness for the second screen:

`gummy --screen {{1}} --temperature {{3800}} --brightness {{65}}`
