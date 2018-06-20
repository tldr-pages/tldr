# neofetch

> CLI system tool to display information about your operating system, software and hardware.

- Call neofetch to return default config. Config file will be created on first run at $HOME/.config/neofetch/config.conf:  

`neofetch`

- Pass specific parameters to alter what gets displayed:

`neofetch --{{opt1}} {{value}} --{{opt2}} {{value}}`

- Enable/disable an info line from appearing in the output. 'infoname' is the function name in the config file, e.g. memory:

`neofetch --{{enable|disable}} {{infoname}}`

- Hide/Show OS architecture:

`neofetch --os_arch {{on|off}}`

- Enable/Disable CPU brand in output:

`neofetch --cpu_brand {{on|off}}`
