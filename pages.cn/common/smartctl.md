# smartctl

> View a disk's SMART data and other information.
> See https://en.wikipedia.org/wiki/S.M.A.R.T for more information.

- View SMART health summary:

`sudo smartctl --health {{/dev/sda}}`

- View device information:

`sudo smartctl --info {{/dev/sda}}`

- Begin a short self-test:

`sudo smartctl --test short {{/dev/sda}}`

- View current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities {{/dev/sda}}`

- View SMART self-test log (if supported):

`sudo smartctl --log selftest {{/dev/sda}}`
