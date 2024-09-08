# blkpr

> Register, reserve, release, preempt, and clear persistent reservations on a block device that supports Persistent Reservations.
> More information: <https://manned.org/blkpr>.

- Register (command) a new reservation with a given key on a given device:

`blkpr {{-c|--command}} register {{-k|--key}} {{reservation_key}} {{path/to/device}}`

- Set the type of an existing reservation to exclusive access:

`blkpr -c reserve {{-k|--key}} {{reservation_key}} {{-t|--type}} exclusive-access {{path/to/device}}`

- Preempt the existing reservation with a given key and replace it with a new reservation:

`blkpr -c preempt {{-K|--oldkey}} {{old_key}} {{-k|--key}} {{new_key}} {{-t|--type}} write-exclusive {{path/to/device}}`

- Release a reservation with a given key and type on a given device:

`blkpr -c release {{-k|--key}} {{reservation_key}} {{-t|--type}} {{reservation_type}} {{path/to/device}}`

- Clear all reservations from a given device:

`blkpr -c clear {{-k|--key}} {{key}} {{path/to/device}}`
