# smartctl

> Monitor disk health including SMART data.
> More information: <https://www.smartmontools.org>.

- Display SMART health summary:

`sudo smartctl --health {{/dev/sdX}}`

- Display device information:

`sudo smartctl --info {{/dev/sdX}}`

- Start a short self-test in the background:

`sudo smartctl --test short {{/dev/sdX}}`

- Display current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities {{/dev/sdX}}`

- Display exhaustive SMART data:

`sudo smartctl --all {{/dev/sdX}}`
