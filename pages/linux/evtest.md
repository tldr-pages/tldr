# evtest

> Display information from input device drivers.
> More information: <https://manned.org/evtest>.

- List all detected input devices:

`sudo evtest`

- Display events from a specific input device:

`sudo evtest /dev/input/event{{number}}`

- Grab the device exclusively, preventing other clients from receiving events:

`sudo evtest --grab /dev/input/event{{number}}`

- Query the state of a specific key or button on an input device:

`sudo evtest --query /dev/input/event{{number}} {{event_type}} {{event_code}}`
