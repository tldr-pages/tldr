# rig

> Utility that will piece together a random first name, last name, street number and address, along with a geographically consistant (ie, they all match the same area) city, state, ZIP code, and area code.
> More information: <https://manpages.ubuntu.com/manpages/focal/man6/rig.6.html>.

- Display a random name (male or female) and address:

`rig`

- Display a [m]ale (or [f]emale) random name and address:

`rig -{{m|f}}`

- Use data files from a specific directory (default is `/usr/share/rig`):

`rig -d {{path/to/directory}}`

- Display a specific `count` of identities:

`rig -c {{count}}`

- Display a specific `count` of female identities:

`rig -f -c {{count}}`
