# neofetch

> Display information about your operating system, software and hardware.
> More information: <https://github.com/dylanaraps/neofetch>.

- Return the default config, and create it if it's the first time the program runs:

`neofetch`

- Trigger an info line from appearing in the output, where 'infoname' is the function name in the config file, e.g. memory:

`neofetch --{{enable|disable}} {{infoname}}`

- Hide/Show OS architecture:

`neofetch --os_arch {{on|off}}`

- Enable/Disable CPU brand in output:

`neofetch --cpu_brand {{on|off}}`
