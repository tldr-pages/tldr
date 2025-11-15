# ip monitor

> Monitor network for state changes.
> More information: <https://manned.org/ip-monitor>.

- Monitor the whole network for state changes:

`ip {{[mo|monitor]}}`

- Specify the type to monitor:

`ip {{[mo|monitor]}} {{link|address|route|neigh|rule|maddress|...}}`

- Replay an event file (can be generated with `rtmon`):

`ip {{[mo|monitor]}} {{[f|file]}} {{path/to/file}}`
