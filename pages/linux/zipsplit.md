# zipsplit

> Read a zipfile and split it into smaller zipfiles.
> More information: <https://manned.org/zipsplit>.

- Split zipfile into pieces that are no larger than a particular size [n]:

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- [p]ause between the creation of each split zipfile:

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- Output the split zipfiles into the `archive` directory:

`zipsplit -b {{archive}} -n {{size}} {{path/to/archive.zip}}`
