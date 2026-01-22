# CONFIG

> Change or query DOSBox settings at runtime; save configs/languages.
> More information: <https://www.dosbox.com/wiki/CONFIG>.

- Write current config to file (local drive):
  `CONFIG -writeconf {{dosbox.conf}}`

- Write current language strings to file:
  `CONFIG -writelang {{dosbox.lang}}`

- Enable secure mode (disables MOUNT/IMGMOUNT/BOOT):
  `CONFIG -securemode`

- Set a property (e.g., CPU cycles):
  `CONFIG -set "cpu cycles={{10000}}"`

- Set property (e.g., disable EMS):
  `CONFIG -set "dos ems=off"`

- Get property value (stored in %CONFIG%):
  `CONFIG -get "cpu core"`
