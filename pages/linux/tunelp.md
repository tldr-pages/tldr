# tunelp

> Set various parameters for parallel port devices for troubleshooting or for better performance.
> Part of `util-linux`.
> More information: <https://manned.org/tunelp>.

- Check the status of a parallel port device:

`tunelp {{[-s|--status]}} {{/dev/lp0}}`

- Reset a given parallel port:

`tunelp {{[-r|--reset]}} {{/dev/lp0}}`

- Use a given IRQ for a device, each one representing an interrupt line:

`tunelp {{[-i|--irq]}} 5 {{/dev/lp0}}`

- Try a given number of times to output a character to the printer before sleeping for a given time:

`tunelp {{[-c|--chars]}} {{times}} {{[-t|--time]}} {{time_in_centiseconds}} {{/dev/lp0}}`

- Enable or disable aborting on error (disabled by default):

`tunelp {{[-a|--abort]}} {{on|off}}`
