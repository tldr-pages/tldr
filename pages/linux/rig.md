# rig

> Utility that will piece together a random first name, last name, street number and address, along with a geographically consistant (ie, they all match the same area) city, state, ZIP code, and area code.
> More information: <https://manpages.ubuntu.com/manpages/focal/man6/rig.6.html>.

- Display a random name (male or female) and address:

`rig`

- Specify male/female name. If neither or both options are selected, RIG uses both female and male names:

`rig {{-m|-f}}`

- Use data files found in *datadir*. Without this  option, the  default  directory  of /usr/share/rig is assumed:

`rig -d {{datadir}}`

- Display a specific `count` of identities:

`rig -c {{count}}`

- Display a specific `count` of female identities:

`rig -f -c {{count}}`
