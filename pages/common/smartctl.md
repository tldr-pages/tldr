# smartctl

> Monitor disk health including SMART data.
> More information: <https://www.smartmontools.org>.

- SMART health summary:

`sudo smartctl --health {{/dev/sdX}}`

- Device information:

`sudo smartctl --info {{/dev/sdX}}`

- Start a short self-test in the background:

`sudo smartctl --test short {{/dev/sdX}}`

- View current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities {{/dev/sdX}}`

- View exhaustive SMART data:

`sudo smartctl --all {{/dev/sdX}}`
