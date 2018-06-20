# neofetch

> CLI system tool to display information about your operating system, software and hardware.

- Call neofetch to return default config:
> NOTE: Will create by default a config file at $HOME/.config/neofetch/config.conf on first run. 

`neofetch`

- Pass specific parameters to alter what gets displayed:

`neofetch --{{opt1}} {{value}} --{{opt2}} {{value}}`

- Disable an info line from appearing in the output:
> NOTE: 'infoname' is the function name from the 'print_info()' function inside the config file.

`neofetch --{{enable|disable}} {{infoname}}`

- Hide/Show OS architecture:

`neofetch --os_arch {{on|off}}`

- Enable/Disable CPU brand in output

`neofetch --cpu_brand {{on|off}}`
