# Xephyr

> A nested X server that runs as an X application.
> More information: <https://manned.org/xserver-xephyr>.

- Create a black window with display ID ":2":

`Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}`

- Start an X application on the new screen:

`DISPLAY=:2 {{command_name}}`
