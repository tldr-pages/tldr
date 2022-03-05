# rfkill

> Enable and disable wireless devices.
> More information: <https://manned.org/rfkill>.

- List devices:

`rfkill`

- Filter by columns:

`rfkill -o {{ID,TYPE,DEVICE}}`

- Block devices by type (e.g. bluetooth, wlan):

`rfkill block {{bluetooth}}`

- Unblock devices by type (e.g. bluetooth, wlan):

`rfkill unblock {{wlan}}`

- Output in JSON format:

`rfkill -J`
