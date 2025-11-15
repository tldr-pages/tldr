# smartctl

> Monitor disk health including SMART data.
> More information: <https://manned.org/smartctl>.

- Display SMART health summary:

`sudo smartctl {{[-H|--health]}} {{/dev/sdX}}`

- Display device information:

`sudo smartctl {{[-i|--info]}} {{/dev/sdX}}`

- Start a short/long self-test in the background:

`sudo smartctl {{[-t|--test]}} {{short|long}} {{/dev/sdX}}`

- Display the self-test log:

`sudo smartctl {{[-l|--log]}} selftest`

- Display current/last self-test status and other SMART capabilities:

`sudo smartctl {{[-c|--capabilities]}} {{/dev/sdX}}`

- Display exhaustive SMART data:

`sudo smartctl {{[-a|--all]}} {{/dev/sdX}}`
