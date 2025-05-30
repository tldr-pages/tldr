# uinput

> An interception tool writes input events to a virtual keyboard device using /dev/uinput.
> More information: <https://gitlab.com/interception/linux/tools/-/tree/master?ref_type=heads#uinput>.

- Show resulting YAML device description merge and exit:

`uinput -p`

- Merge YAML device description(s) to resulting virtual device (repeatable):

`uinput -c {{device.yaml}}`

- Merge reference device description from device node(s) to resulting virtual device (repeatable):

`uinput -d {{devnode}}`
