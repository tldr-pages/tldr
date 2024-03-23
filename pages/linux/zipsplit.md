# zipsplit

> Read a Zip archive and split it into smaller Zip archives.
> More information: <https://manned.org/zipsplit>.

- Split Zip archive into pieces that are no larger than 36000 bytes:

`zipsplit {{path/to/archive.zip}}`

- Use a given [n]umber of bytes as the piece limit:

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- [p]ause between the creation of each split Zip archive:

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- Output the split Zip archives into a given directory:

`zipsplit -b {{path/to/output_directory}} -n {{size}} {{path/to/archive.zip}}`
