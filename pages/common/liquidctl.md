# liquidctl

> Control liquid coolers.
> More information: <https://github.com/liquidctl/liquidctl>.

- List available devices:

`liquidctl list`

- Initialize all supported devices:

`sudo liquidctl initialize all`

- Print the status of available liquid coolers:

`liquidctl status`

- Match a string in product name to pick a device and set its speed to a flat 50%:

`liquidctl {{[-m|--match]}} {{string}} set {{fan|pump|...}} speed 50`

- Set a gradual fan speed curve that is 0% at 20°C, 50% at 50°C, and 100% at 70°C:

`liquidctl set {{fan|pump|...}} speed 20 0 50 50 70 100`

- Set the liquid cooler RGB lights (supported modes depend on the model):

`liquidctl set {{fan|pump|...}} color {{fixed|fading|rainbow|...}} {{00ff00|'rgb(255,0,0)'|'hsv(120,100,100)'|...}}`
