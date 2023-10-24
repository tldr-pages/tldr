# hipstopgm

> Read a HIPS file as input and return a PGM image as output.
> If the HIPS file contains more than one frame in sequence, `hipstopgm` will concatenate all the frames vertically.
> More information: <https://netpbm.sourceforge.net/doc/hipstopgm.html>.

- Convert a HIPS file into a PGM image:

`hipstopgm {{path/to/file.hips}}`

- Suppress all informational messages:

`hipstopgm -quiet`

- Display version:

`hipstopgm -version`
