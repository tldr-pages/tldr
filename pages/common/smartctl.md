# smartctl

> View a disk's [SMART](https://en.wikipedia.org/wiki/S.M.A.R.T.) data and other information.

- View SMART health summary:

`sudo smartctl --health {{/dev/<device>}}`

- View device information:

`sudo smartctl --info {{/dev/<device>}}`

- Begin a (short) self-test:

`sudo smartctl --test {{short}} {{/dev/<device>}}`

- View current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities {{/dev/<device>}}`

- View SMART self-test log (if supported):

`sudo smartctl --log selftest {{/dev/<device>}}`
