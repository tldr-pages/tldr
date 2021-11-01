# ddcutil

> Control the settings of connected displays via DDC/CI.
> More information: <https://www.ddcutil.com>.

- List all compatible displays:

`ddcutil detect`

- Change the brightness (option 0x10) of display 1 to 50%:

`ddcutil -d {{1}} setvcp {{10}} {{50}}`

- Increase the contrast (option 0x12) of display 1 by 5%:

`ddcutil -d {{1}} setvcp {{12}} {{+}} {{5}}`

- Read the settings of display 1:

`ddcutil -d {{1}} getvcp ALL`
