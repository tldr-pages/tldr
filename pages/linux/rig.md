# rig

> Utility that will piece together a random first name, last name, street number and address, along with a geographically consistant (ie, they all match the same area) city, state, ZIP code, and area code.
> More information: <http://manpages.ubuntu.com/manpages/bionic/man6/rig.6.html>.

- Return a random name and address:

`rig`

- Specify male/female name. If neither or both options are selected, RIG uses both female and male names:

`rig -m`

- Use data files found in *datadir*. Without this  option, the  default  directory  of /usr/share/rig is assumed:

`rig -d {{datadir}}`

- Output *num* identities. Default is 1:

`rig -c {{num}}`

- Return *num* identities for both male/female:

`rig -m -f -c {{num}}`
