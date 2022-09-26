# ufraw-batch

> Convert RAW files from cameras into standard image files.
> More information: <https://manned.org/ufraw-batch>.

- Simply convert RAW files to JPG:

`ufraw-batch --out-type=jpg {{input_file(s)}}`

- Simply convert RAW files to PNG:

`ufraw-batch --out-type=png {{input_file(s)}}`

- Extract the preview image from the raw file:

`ufraw-batch --embedded-image {{input_file(s)}}`

- Save the file with size up to the given maximums MAX1 and MAX2:

`ufraw-batch --size=MAX1,MAX2 {{input_file(s)}}`
