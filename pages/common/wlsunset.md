# wlsunset

> Adjust the color temperature in Wayland compositors depending on the sunset/sunrise times.
> More information: <https://manned.org/wlsunset>.

- Automatically compute sunset/sunrise times based on the specified location:

`wlsunset -l {{latitude}} -L {{longitude}}`

- Manually set the sunset/sunrise times (time format: `HH:MM`):

`wlsunset -s {{sunset_time}} -S {{sunrise_time}}`

- Set the high and low temperatures (default: high - 6500, low - 4000):

`wlsunset -T {{high_temp}} -t {{low_temp}}`

- Set the animation time to `n` seconds (only applicable when using manual sunset/sunrise times):

`wlsunset -d {{n}} -s {{sunset_time}} -S {{sunrise_time}}`

- Set the gamma (default: 1.0):

`wlsunset -g {{gamma_value}}`
