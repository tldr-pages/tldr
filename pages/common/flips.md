# flips

> Create and apply patches for IPS and BPS files.
> More information: <https://github.com/Alcaro/Flips>.

- Start Flips to create and apply patches interactively:

`flips`

- Apply a patch and create a new ROM file:

`flips --apply {{patch.bps}} {{rom.smc}} {{hack.smc}}`

- Create a patch from two ROMs:

`flips --create {{rom.smc}} {{hack.smc}} {{patch.bps}}`
