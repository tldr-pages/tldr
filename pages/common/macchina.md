# macchina

> Macchina is a tool which fetches and displays information about your computer.
> More information: <https://github.com/Macchina-CLI/macchina>.

- List out system information, with either default settings or those specified in your configuration file:

`macchina`

- Specify a custom configuration file path:

`macchina --config {{path/to/configuration/file}}`

- List out system information, but lengthen uptime, shell and kernel output:

`macchina --long-uptime --long-shell --long-kernel`

- Check for any errors / system failures encountered when trying to fetch system information:

`macchina --doctor`

- List out original artists of all the ASCII art used by macchina:

`macchina --ascii-artists`
