# smartctl

> View a disk's SMART data and other information.
> More information: <https://en.wikipedia.org/wiki/S.M.A.R.T.>.

- View SMART health summary:

`sudo smartctl --health {{/dev/sdX}}`

- View device information:

`sudo smartctl --info {{/dev/sdX}}`

- Begin a short self-test:

`sudo smartctl --test short {{/dev/sdX}}`

- View current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities {{/dev/sdX}}`

- View SMART self-test log (if supported):

`sudo smartctl --log selftest {{/dev/sdX}}`
