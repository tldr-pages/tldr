# zipsplit

> Split a Zip archive into smaller Zip archives.
> More information: <https://manned.org/zipsplit>.

- Split Zip archive into parts that are no larger than 36000 bytes (36 MB):

`zipsplit {{path/to/archive.zip}}`

- Use a given [n]umber of bytes as the part limit:

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- [p]ause between the creation of each part:

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- Output the smaller Zip archives into a given directory:

`zipsplit -b {{path/to/output_directory}} -n {{size}} {{path/to/archive.zip}}`
