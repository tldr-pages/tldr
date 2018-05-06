# rtcwake

> Enter a system sleep state until specified wakeup time relative to your bios clock.
> Commands need to be run as superuser since shutdowns are involved.

- Check your hardware clock info and exit:

`rtcwake -m show -v`

- Show if an allarm is set:

`rtcwake -m show`

- Disable a previous set alarm:

`rtc -m disable`

- Suspend to ram and wakeup after 10 seconds:

`# rtcwake -m mem -s {{10}}`

- Suspend to disk _(higher power saving)_ and wakeup 10 minutes later:

`# rtcwake -m disk --date +{{15}}m`

- Suspend to disk and wakeup 1 hour later so play some music with mpv:

`# rtcwake -m disk --date +{{1}}h && mpv {{music_folder/*}}`

- Freeze the system _(more efficent than suspend-to-ram but linux > 3.9 required)_ and wakeup at a given date and time:

`# rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- Run a test _(CTRL-C to abort)_ in which the computer is waked at a given time:

`rtcwake -m on --date {{hh:ss}}`
