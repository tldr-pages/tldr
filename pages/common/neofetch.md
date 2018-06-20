# neofetch

> CLI system tool to display information about your operating system, software and hardware.

- Call neofetch to return the default config, and create it if it's the first time the program runs:

`neofetch`

- Pass specific parameters to alter what gets displayed:

`neofetch --{{opt1}} {{value}} --{{opt2}} {{value}}`

- Trigger an info line from appearing in the output, where 'infoname' is the function name in the config file, e.g. memory:

`neofetch --{{enable|disable}} {{infoname}}`

- Hide/Show OS architecture:

`neofetch --os_arch {{on|off}}`

- Enable/Disable CPU brand in output:

`neofetch --cpu_brand {{on|off}}`
