# sprio

> View factors that comprise a job's scheduling priority.
> More information: <https://manned.org/sprio>.

- List all pending jobs with their weighted priorities:

`sprio`

- List all pending jobs with their [norm]alized priorities:

`sprio --norm`

- List priorities for specific jobs:

`sprio --jobs={{1..infinity,1..infinity,...}}`

- List priorities for specific users:

`sprio --users={{username1,username2,...}}`

- List configured weights for each priority component:

`sprio --weights`
