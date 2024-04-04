# tlp-stat

> Generate TLP status reports.
> See also `tlp`.
> More information: <https://linrunner.de/tlp/usage/tlp-stat>.

- Generate status report with configuration and all active settings:

`sudo tlp-stat`

- Show information about various devices:

`sudo tlp-stat --{{battery|disk|processor|graphics|pcie|rfkill|usb}}`

- Show verbose information about devices that support verbosity:

`sudo tlp-stat --verbose --{{battery|processor|pcie|usb}}`

- Show configuration:

`sudo tlp-stat {{-c|--config}}`

- Monitor [p]ower supply `udev` [ev]ents:

`sudo tlp-stat {{-P|--pev}}`

- Show [p]ower [sup]ply diagonistics:

`sudo tlp-stat --psup`

- Show [temp]eratures and fan speed:

`sudo tlp-stat {{-t|--temp}}`

- Show general system information:

`sudo tlp-stat {{-s|--system}}`
