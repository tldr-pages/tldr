# liquidctl

> Control liquid coolers.
> More information: <https://github.com/liquidctl/liquidctl>.

- List available devices:

`liquidctl list`

- Initialize all supported devices:

`sudo liquidctl initialize all`

- Print the status of available liquid coolers:

`liquidctl status`

- Match with a string in product name and set fan speed to 0% in 20°C, 50% in 50°C and 100% in 70°C:

`liquidctl --match {{string}} set fan speed {{20 0 50 50 70 100}}`
