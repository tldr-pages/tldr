# rtcwake

> Enter a system sleep state until specified wakeup time relative to your BIOS clock.
> More information: <https://manned.org/rtcwake>.

- Show whether an alarm is set or not:

`sudo rtcwake -m show -v`

- Suspend to RAM and wakeup after 10 seconds:

`sudo rtcwake -m mem -s {{10}}`

- Suspend to disk (higher power saving) and wakeup 15 minutes later:

`sudo rtcwake -m disk --date +{{15}}min`

- Freeze the system (more efficient than suspend-to-RAM but version 3.9 or newer of the Linux kernel is required) and wakeup at a given date and time:

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- Disable a previously set alarm:

`sudo rtcwake -m disable`

- Perform a dry run to wakeup the computer at a given time. (Press Ctrl + C to abort):

`sudo rtcwake -m on --date {{hh:ss}}`
