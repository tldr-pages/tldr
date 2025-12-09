# neofetch

> Display information about the operating system, software and hardware.
> Note: `neofetch` is no longer maintained.
> See also: `fastfetch`.
> More information: <https://manned.org/neofetch>.

- Return the default config, and create it if it's the first time the program runs:

`neofetch`

- Trigger an info line from appearing in the output, where `infoname` is the function name in the configuration file, e.g. memory:

`neofetch --{{enable|disable}} {{infoname}}`

- Hide/Show OS architecture:

`neofetch --os_arch {{on|off}}`

- Enable/Disable CPU brand in output:

`neofetch --cpu_brand {{on|off}}`
