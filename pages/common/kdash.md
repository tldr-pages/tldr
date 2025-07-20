# kdash

> A simple terminal dashboard for Kubernetes.
> Mode information: <https://github.com/kdash-rs/kdash/#usage>.

- Show dashboard:

`kdash`

- Show dashboard in debug mode and write logs to a file in the current directory:

`kdash {{[-d|--debug]}}`

- Set the tick rate:

`kdash {{[-t|--tick-rate]}} {{100}}`

- Set the polling rate (must be a multiple of the tick rate):

`kdash {{[-t|--tick-rate]}} {{200}} {{[-p|--poll-rate]}} {{400}}`
