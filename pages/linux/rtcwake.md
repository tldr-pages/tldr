# rtcwake

> Enter a system sleep state until specified wakeup time relative to your BIOS clock.
> More information: <https://manned.org/rtcwake>.

- Show whether an alarm is set or not:

`sudo rtcwake {{[-m|--mode]}} show {{[-v|--verbose]}}`

- Suspend to RAM and wakeup after 10 seconds:

`sudo rtcwake {{[-m|--mode]}} mem {{[-s|--seconds]}} {{10}}`

- Suspend to disk (higher power saving) and wakeup 15 minutes later:

`sudo rtcwake {{[-m|--mode]}} disk --date +{{15}}min`

- Freeze the system (more efficient than suspend-to-RAM but version 3.9 or newer of the Linux kernel is required) and wakeup at a given date and time:

`sudo rtcwake {{[-m|--mode]}} freeze --date {{YYYYMMDDhhmm}}`

- Disable a previously set alarm:

`sudo rtcwake {{[-m|--mode]}} disable`

- Perform a dry run to wakeup the computer at a given time. (Press `<Ctrl c>` to abort):

`sudo rtcwake {{[-m|--mode]}} on --date {{hh:ss}}`
