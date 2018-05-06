# rtcwake

> Enter a system sleep state until specified wakeup time relative to your bios clock.
> Commands need to be run as superuser since shutdowns are involved.

- Check your hardware clock info and exit:

`rtcwake -m show -v`

- Show if an alarm is set:

`rtcwake -m show`

- Disable a previous set alarm:

`rtc -m disable`

- Suspend to ram and wakeup after 10 seconds:

`sudo rtcwake -m mem -s {{10}}`

- Suspend to disk (higher power saving) and wakeup 10 minutes later:

`sudo rtcwake -m disk --date +{{15}}m`

- Suspend to disk and wakeup 1 hour later and play some music with mpv:

`sudo rtcwake -m disk --date +{{1}}h && mpv {{music_folder/*}}`

- Freeze the system (more efficent than suspend-to-ram but linux > 3.9 required) and wakeup at a given date and time:

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- Run a test (CTRL-C to abort) in which the computer is waked at a given time:

`rtcwake -m on --date {{hh:ss}}`
