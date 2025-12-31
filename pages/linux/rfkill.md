# rfkill

> Enable and disable wireless devices.
> More information: <https://manned.org/rfkill>.

- List devices:

`rfkill`

- Filter by columns:

`rfkill {{[-o|--output]}} {{ID,TYPE,DEVICE,...}}`

- Block devices by type:

`rfkill block {{bluetooth|wifi|gps|nfc|...}}`

- Unblock devices by type:

`rfkill unblock {{bluetooth|wifi|gps|nfc|...}}`

- Output in JSON format:

`rfkill {{[-J|--json]}}`
