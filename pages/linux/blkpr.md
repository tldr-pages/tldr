# blkpr

> Register, reserve, release, preempt, and clear persistent reservations on a block device that supports Persistent Reservations.
> More information: <https://manned.org/blkpr>.

- Register ([c]ommand) a new reservation with a given [k]ey on a given device:

`blkpr {{-c|--command}} register --key {{reservation_key}} {{path/to/device}}`

- Set the [t]ype an existing reservation to exclusive access:

`blkpr -c reserve -k {{reservation_key}} {{-t|--type}} exclusive-access {{path/to/device}}`

- Preempt the existing reservation with a specific [K]ey and replaces it with a new reservation:

`blkpr -c preempt {{-K|--oldkey}} {{old_key}} --key {{new_key}} -t write-exclusive {{path/to/device}}`

- Clear all reservations from a specific device:

`blkpr -c clear -k {{key}} {{path/to/device}}`
