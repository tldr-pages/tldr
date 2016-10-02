# pmset

> Configure macOS power management settings, as one might do in System Preferences > Energy Saver.
> Commands that modify settings must begin with `sudo`.

- Display the current power management settings:

`pmset -g`

- Display the current power source and battery levels:

`pmset -g batt`

- Set display to never sleep when on charger power:

`sudo pmset -c displaysleep 0`

- Set display to sleep after 15 minutes when on battery power:

`sudo pmset -b displaysleep 15`

- Schedule computer to automatically wake up every weekday at 9 AM:

`sudo pmset repeat wake MTWRF 09:00:00`

- Restore to system defaults:

`sudo pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1`
