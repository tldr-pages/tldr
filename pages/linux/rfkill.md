# rfkill

> Enable and disable wireless devices.

- List devices:

`rfkill list {{all}}`

- Block by type (e.g. bluetooth, wlan):

`rfkill block {{bluetooth}}`

- Unblock by type (e.g. bluetooth, wlan):

`rfkill unblock {{wlan}}`

- Filter by columns:

`rfkill -o {{COL1,COL2,COL3}}`

- Output JSON:

`rfkill -J`
