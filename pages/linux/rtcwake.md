# rtcwake

> Enter a system sleep state until specified wakeup time relative to your bios clock.

- Show whether an alarm is set or not:

`sudo rtcwake -m show -v`

- Suspend to ram and wakeup after 10 seconds:

`sudo rtcwake -m mem -s {{10}}`

- Suspend to disk (higher power saving) and wakeup 15 minutes later:

`sudo rtcwake -m disk --date +{{15}}m`

- Suspend to disk and wakeup 1 hour later and play some music with mpv:

`sudo rtcwake -m disk --date +{{1}}h && mpv {{music_folder/*}}`

- Freeze the system (more efficent than suspend-to-ram but linux > 3.9 required) and wakeup at a given date and time:

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- Disable a previously set alarm:

`sudo rtc -m disable`

- Run a test (CTRL-C to abort) in which the computer is waked at a given time:

`sudo rtcwake -m on --date {{hh:ss}}`
