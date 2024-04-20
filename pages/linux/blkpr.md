# blkpr

> Register, reserve, release, preempt, and clear persistent reservations on a block device that supports Persistent Reservations.
> More information: <https://manned.org/blkpr>.

- Register ([c]ommand) a new reservation with a given [k]ey on a given device:

`blkpr {{-c|--command}} register --key {{reservation_key}} {{path/to/device}}`

- Set the [t]ype of an existing reservation to exclusive access:

`blkpr -c reserve -k {{reservation_key}} {{-t|--type}} exclusive-access {{path/to/device}}`

- Preempt the existing reservation with a given [K]ey and replace it with a new reservation:

`blkpr -c preempt {{-K|--oldkey}} {{old_key}} --key {{new_key}} -t write-exclusive {{path/to/device}}`

- Release a reservation with a given [k]ey and [t]ype on a given device:

`blkpr -c release --key {{reservation_key}} -t {{reservation_type}} {{path/to/device}}`

- Clear all reservations from a given device:

`blkpr -c clear -k {{key}} {{path/to/device}}`
