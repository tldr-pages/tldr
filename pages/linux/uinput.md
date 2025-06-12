# uinput

> Intercept and write input events to a virtual keyboard device using /dev/uinput.
> More information: <https://gitlab.com/interception/linux/tools/-/tree/master#uinput>.

- Show resulting YAML device description merge and exit (dry-run):

`uinput -p`

- Merge YAML device description(s) to resulting virtual device:

`sudo uinput -c {{path/to/device1.yaml path/to/device2.yaml ...}}`

- Merge reference device description from device node(s) to resulting virtual device:

`sudo uinput -d {{/dev/input/eventX /dev/input/eventY ...}}`
