# ufraw-batch

> Convert RAW files from cameras into standard image files.
> More information: <https://manned.org/ufraw-batch>.

- Simply convert RAW files to JPG:

`ufraw-batch --out-type=jpg {{path/to/file}}`

- Simply convert RAW files to PNG:

`ufraw-batch --out-type=png {{path/to/file}}`

- Extract the preview image from the raw file:

`ufraw-batch --embedded-image {{path/to/file}}`

- Save the file with size up to the given maximums MAX1 and MAX2:

`ufraw-batch --size=MAX1,MAX2 {{path/to/file}}`
