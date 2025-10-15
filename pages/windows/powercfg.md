# powercfg

> Configure power settings and manage power schemes.
> More information: <https://learn.microsoft.com/windows-hardware/design/device-experiences/powercfg-command-line-options>.

- Display the current power scheme:

`powercfg /getactivescheme`

- List all available power schemes:

`powercfg {{[/L|/list]}}`

- Set the active power scheme by its GUID:

`powercfg /setactive {{GUID}}`

- Turn off the display after a specific number of minutes on AC power:

`powercfg {{[/X|/change]}} monitor-timeout-ac {{minutes}}`

- Turn off the display after a specific number of minutes on battery power:

`powercfg {{[/X|/change]}} monitor-timeout-dc {{minutes}}`

- Put the system to sleep after a specific number of minutes on AC power:

`powercfg {{[/X|/change]}} standby-timeout-ac {{minutes}}`

- Generate a system sleep diagnostics report and save it to a file:

`powercfg /sleepstudy /output {{path\to\report.html}}`

- Generate a full power efficiency report and save it to a file:

`powercfg /energy /output {{path\to\report.html}}`
